from __future__ import annotations

import argparse

from utils import format_example

from arc2.shared.discovery import TaskSpec, iter_task_specs, load_task_spec
from arc2.shared.render import load_task_examples


def verify_official_examples(spec: TaskSpec) -> dict[str, object]:
    if spec.reference_task_path is None:
        raise ValueError(f"task {spec.task_id} has no REFERENCE_TASK_PATH")

    examples = load_task_examples(spec.reference_task_path)
    failures: list[str] = []
    for idx, example in enumerate(examples):
        if "output" not in example:
            failures.append(f"example {idx:02d}: missing output")
            continue
        formatted = format_example(example)
        try:
            actual = spec.verifier(formatted["input"])
        except Exception as exc:
            failures.append(f"example {idx:02d}: {type(exc).__name__}: {exc}")
            continue
        if actual != formatted["output"]:
            failures.append(f"example {idx:02d}: output mismatch")

    return {
        "task_id": spec.task_id,
        "total": len(examples),
        "passed": len(examples) - len(failures),
        "failures": failures,
    }


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify ARC2 verifiers on official examples.")
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
            result = verify_official_examples(spec)
        except Exception as exc:
            print(f"fail {spec.task_id}: {type(exc).__name__}: {exc}")
            all_passed = False
            continue

        failures = result["failures"]
        if failures:
            print(f"fail {spec.task_id}: {result['passed']}/{result['total']} official examples passed")
            for failure in failures:
                print(f"  {failure}")
            all_passed = False
            continue

        print(f"pass {spec.task_id}: {result['passed']}/{result['total']} official examples passed")

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
