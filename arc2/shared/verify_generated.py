from __future__ import annotations

import argparse
import json
from pathlib import Path

from arc2.shared.discovery import TaskSpec, iter_task_specs, load_task_spec
from arc2.shared.paths import examples_dir
from arc2.shared.verify import verify_examples


def load_generated_examples(path: Path) -> tuple[list[dict], list[str]]:
    if not path.exists():
        raise FileNotFoundError(path)
    if not path.is_dir():
        raise NotADirectoryError(path)

    example_paths = sorted(path.glob("*.json"))
    if not example_paths:
        raise FileNotFoundError(f"no generated example json files found in {path}")

    examples: list[dict] = []
    labels: list[str] = []
    for example_path in example_paths:
        with open(example_path, "r") as fp:
            examples.append(json.load(fp))
        labels.append(example_path.name)
    return examples, labels


def verify_generated_examples(spec: TaskSpec) -> dict[str, object]:
    task_examples_dir = examples_dir(spec.task_id)
    examples, labels = load_generated_examples(task_examples_dir)
    return verify_examples(spec, examples, example_labels=labels)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify ARC2 verifiers on generated examples.")
    parser.add_argument("--task", help="Task id or task package name. Verifies all tasks if omitted.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        specs = [load_task_spec(args.task)] if args.task else list(iter_task_specs())
    except Exception as exc:
        task_name = args.task or "all tasks"
        print(f"fail {task_name}: {type(exc).__name__}: {exc}")
        return 1

    all_passed = True
    for spec in specs:
        try:
            result = verify_generated_examples(spec)
        except Exception as exc:
            print(f"fail {spec.task_id}: {type(exc).__name__}: {exc}")
            all_passed = False
            continue

        failures = result["failures"]
        if failures:
            print(f"fail {spec.task_id}: {result['passed']}/{result['total']} generated examples passed")
            for failure in failures:
                print(f"  {failure}")
            all_passed = False
            continue

        print(f"pass {spec.task_id}: {result['passed']}/{result['total']} generated examples passed")

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
