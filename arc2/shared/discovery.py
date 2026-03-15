from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from pathlib import Path
from types import ModuleType
from typing import Callable, Iterator
import pkgutil

import arc2.tasks as tasks_pkg

from arc2.shared.paths import task_artifacts_dir, task_package_name
from arc2.shared.paths import REPO_ROOT


@dataclass(frozen=True)
class TaskSpec:
    task_id: str
    package_name: str
    task_dir: Path
    artifacts_dir: Path
    generator: Callable[[float, float], dict]
    verifier: Callable
    reference_task_path: Path | None


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


def _load_task_module(task_name: str) -> ModuleType:
    package_name = task_package_name(task_name)
    return import_module(f"{tasks_pkg.__name__}.{package_name}")


def load_task_spec(task_name: str) -> TaskSpec:
    module = _load_task_module(task_name)
    task_id = getattr(module, "TASK_ID")
    task_dir = Path(module.__file__).resolve().parent
    return TaskSpec(
        task_id=task_id,
        package_name=module.__name__.split(".")[-1],
        task_dir=task_dir,
        artifacts_dir=task_artifacts_dir(task_id),
        generator=getattr(module, "generate"),
        verifier=getattr(module, "verify"),
        reference_task_path=_normalize_reference_path(module),
    )


def iter_task_specs() -> Iterator[TaskSpec]:
    for module_info in sorted(pkgutil.iter_modules(tasks_pkg.__path__), key=lambda item: item.name):
        if module_info.ispkg and module_info.name.startswith("task_"):
            yield load_task_spec(module_info.name)


def list_task_ids() -> list[str]:
    return [spec.task_id for spec in iter_task_specs()]
