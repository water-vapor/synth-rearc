from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
ARC2_ROOT = REPO_ROOT / "arc2"
TASKS_ROOT = ARC2_ROOT / "tasks"
ARTIFACTS_ROOT = ARC2_ROOT / "artifacts"


def task_package_name(task_name: str) -> str:
    return task_name if task_name.startswith("task_") else f"task_{task_name}"


def task_dir(task_name: str) -> Path:
    return TASKS_ROOT / task_package_name(task_name)


def task_artifacts_dir(task_id: str) -> Path:
    return ARTIFACTS_ROOT / task_id


def examples_dir(task_id: str) -> Path:
    return task_artifacts_dir(task_id) / "examples"


def previews_dir(task_id: str) -> Path:
    return task_artifacts_dir(task_id) / "previews"

