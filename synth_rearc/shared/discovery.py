from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Callable, Iterator
import pkgutil

import synth_rearc.tasks as tasks_pkg

from synth_rearc.shared.paths import OFFICIAL_DATA_ROOT, REPO_ROOT, official_task_path
from synth_rearc.shared.paths import task_artifacts_dir, task_package_name


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    package_name: str
    task_dir: Path
    dataset: str
    split: str
    artifacts_dir: Path
    generator: Callable[[float, float], dict]
    verifier: Callable
    reference_task_path: Path
    max_examples: int | None


def _normalize_reference_path(module: ModuleType) -> Path | None:
    reference_path = getattr(module, "REFERENCE_TASK_PATH", None)
    if reference_path is None:
        return None
    candidate = Path(reference_path)
    if candidate.is_absolute():
        return candidate
    task_relative_candidate = Path(module.__file__).resolve().parent / candidate
    if task_relative_candidate.exists():
        return task_relative_candidate
    return REPO_ROOT / candidate


def _infer_dataset_split(reference_path: Path | None) -> tuple[str | None, str | None]:
    if reference_path is None:
        return None, None
    try:
        relative = reference_path.relative_to(OFFICIAL_DATA_ROOT)
    except ValueError:
        return None, None
    if len(relative.parts) < 3:
        return None, None
    dataset, split = relative.parts[:2]
    return dataset, split


def _resolve_reference_path(
    module: ModuleType,
    task_id: str,
    *,
    dataset: str | None = None,
    split: str | None = None,
) -> Path:
    if (dataset is None) != (split is None):
        raise ValueError("dataset and split must be provided together")
    if dataset is not None and split is not None:
        path = official_task_path(dataset, split, task_id)
        if not path.exists():
            raise FileNotFoundError(path)
        return path
    reference_path = _normalize_reference_path(module)
    if reference_path is None:
        raise ValueError(f"task {task_id} does not declare REFERENCE_TASK_PATH")
    return reference_path


def _load_task_module(task_name: str) -> ModuleType:
    package_name = task_package_name(task_name)
    return import_module(f"{tasks_pkg.__name__}.{package_name}")


def load_task_spec(
    task_name: str,
    *,
    dataset: str | None = None,
    split: str | None = None,
) -> TaskSpec:
    module = _load_task_module(task_name)
    task_id = getattr(module, "TASK_ID")
    task_dir = Path(module.__file__).resolve().parent
    reference_task_path = _resolve_reference_path(module, task_id, dataset=dataset, split=split)
    resolved_dataset, resolved_split = _infer_dataset_split(reference_task_path)
    if resolved_dataset is None or resolved_split is None:
        raise ValueError(f"could not infer dataset/split from {reference_task_path}")
    return TaskSpec(
        task_id=task_id,
        package_name=module.__name__.split(".")[-1],
        task_dir=task_dir,
        dataset=resolved_dataset,
        split=resolved_split,
        artifacts_dir=task_artifacts_dir(task_id, resolved_dataset, resolved_split),
        generator=getattr(module, "generate"),
        verifier=getattr(module, "verify"),
        reference_task_path=reference_task_path,
        max_examples=getattr(module, "MAX_EXAMPLES", None),
    )


def iter_task_specs(
    *,
    dataset: str | None = None,
    split: str | None = None,
) -> Iterator[TaskSpec]:
    for module_info in sorted(pkgutil.iter_modules(tasks_pkg.__path__), key=lambda item: item.name):
        if module_info.ispkg and module_info.name.startswith("task_"):
            try:
                yield load_task_spec(module_info.name, dataset=dataset, split=split)
            except FileNotFoundError:
                if dataset is not None and split is not None:
                    continue
                raise


def list_task_ids() -> list[str]:
    return [spec.task_id for spec in iter_task_specs()]
