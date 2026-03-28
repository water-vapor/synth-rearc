from __future__ import annotations

from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PACKAGE_ROOT = REPO_ROOT / "synth_rearc"
TASKS_ROOT = PACKAGE_ROOT / "tasks"
DATA_ROOT = REPO_ROOT / "data"
OFFICIAL_DATA_ROOT = DATA_ROOT / "official"
TASK_LISTS_ROOT = DATA_ROOT / "task_lists"
PROMPTS_ROOT = REPO_ROOT / "prompts"
ARTIFACTS_ROOT = REPO_ROOT / "artifacts"


def task_package_name(task_name: str) -> str:
    return task_name if task_name.startswith("task_") else f"task_{task_name}"


def task_dir(task_name: str) -> Path:
    return TASKS_ROOT / task_package_name(task_name)


def official_task_path(dataset: str, split: str, task_id: str) -> Path:
    return OFFICIAL_DATA_ROOT / dataset / split / f"{task_id}.json"


def task_artifacts_dir(task_id: str, dataset: str, split: str) -> Path:
    return ARTIFACTS_ROOT / dataset / split / task_id


def previews_dir(task_id: str, dataset: str, split: str) -> Path:
    return task_artifacts_dir(task_id, dataset, split) / "previews"
