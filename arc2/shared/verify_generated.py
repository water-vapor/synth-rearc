from __future__ import annotations

import argparse
from pathlib import Path

from arc2.shared.discovery import TaskSpec, iter_task_specs, load_task_spec
from arc2.shared.render import load_task_examples
from arc2.shared.verify import verify_examples


def load_generated_examples(path: Path) -> tuple[list[dict], list[str]]:
    examples = load_task_examples(path)
    labels = [f"task.json[{idx:03d}]" for idx in range(len(examples))]
    return examples, labels


def verify_generated_examples(spec: TaskSpec) -> dict[str, object]:
    task_path = spec.artifacts_dir / "task.json"
    examples, labels = load_generated_examples(task_path)
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
