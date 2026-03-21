from __future__ import annotations

import argparse
import json
from pathlib import Path
from random import seed as set_seed
import shutil

from utils import is_grid

from arc2.shared.discovery import TaskSpec, iter_task_specs, load_task_spec
from arc2.shared.paths import previews_dir
from arc2.shared.render import load_task_examples, save_example_sheet, save_preview_batches


def _clear_files(directory: Path, pattern: str) -> None:
    if not directory.exists():
        return
    for path in directory.glob(pattern):
        path.unlink()


def generate_verified_examples(
    spec: TaskSpec,
    *,
    n_examples: int,
    diff_lb: float,
    diff_ub: float,
) -> list[dict]:
    examples: list[dict] = []
    seen = set()
    attempts = 0
    if spec.max_examples is not None:
        n_examples = min(n_examples, spec.max_examples)
    max_attempts = max(1000, n_examples * 200)
    while len(examples) < n_examples:
        attempts += 1
        if attempts > max_attempts:
            raise RuntimeError(f"failed to generate {n_examples} unique examples for {spec.task_id}")
        example = spec.generator(diff_lb, diff_ub)
        if not is_grid(example["input"]) or not is_grid(example["output"]):
            raise ValueError(f"task {spec.task_id} returned an invalid grid")
        if spec.verifier(example["input"]) != example["output"]:
            raise ValueError(f"task {spec.task_id} generated an unverifiable example")
        if example["input"] == example["output"]:
            continue
        if example["input"] in seen:
            continue
        seen.add(example["input"])
        examples.append(example)
    return examples


def save_examples(spec: TaskSpec, examples: list[dict]) -> tuple[Path, Path]:
    task_artifacts_dir = spec.artifacts_dir
    task_previews_dir = previews_dir(spec.task_id)
    task_artifacts_dir.mkdir(parents=True, exist_ok=True)
    task_previews_dir.mkdir(parents=True, exist_ok=True)

    legacy_examples_dir = task_artifacts_dir / "examples"
    if legacy_examples_dir.exists():
        shutil.rmtree(legacy_examples_dir)
    _clear_files(task_previews_dir, "*.png")

    task_path = task_artifacts_dir / "task.json"
    with open(task_path, "w") as fp:
        json.dump(examples, fp)

    return task_path, task_previews_dir


def maybe_render_originals(spec: TaskSpec) -> Path | None:
    if spec.reference_task_path is None:
        return None
    reference_examples = load_task_examples(spec.reference_task_path)
    originals_path = previews_dir(spec.task_id) / "originals.png"
    save_example_sheet(reference_examples, originals_path, title=f"{spec.task_id} originals", show_index=False)
    return originals_path


def build_task(
    spec: TaskSpec,
    *,
    n_examples: int,
    diff_lb: float,
    diff_ub: float,
) -> dict[str, object]:
    examples = generate_verified_examples(spec, n_examples=n_examples, diff_lb=diff_lb, diff_ub=diff_ub)
    task_path, task_previews_dir = save_examples(spec, examples)
    preview_paths = save_preview_batches(examples, task_previews_dir)
    originals_path = maybe_render_originals(spec)
    return {
        "task_id": spec.task_id,
        "task_json": task_path,
        "preview_paths": preview_paths,
        "originals_path": originals_path,
        "n_examples": len(examples),
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Build ARC2 task artifacts.")
    parser.add_argument("--task", help="Task id or task package name. Builds all tasks if omitted.")
    parser.add_argument("--n-examples", type=int, default=100)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--diff-lb", type=float, default=0.0)
    parser.add_argument("--diff-ub", type=float, default=1.0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    set_seed(args.seed)
    specs = [load_task_spec(args.task)] if args.task else list(iter_task_specs())
    for spec in specs:
        result = build_task(spec, n_examples=args.n_examples, diff_lb=args.diff_lb, diff_ub=args.diff_ub)
        print(f"built {result['task_id']} -> {result['task_json']}")
        for preview_path in result["preview_paths"]:
            print(f"preview {preview_path}")
        if result["originals_path"] is not None:
            print(f"originals {result['originals_path']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
