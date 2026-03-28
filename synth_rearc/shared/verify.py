from __future__ import annotations

import argparse
from collections.abc import Sequence

from utils import format_example

from synth_rearc.shared.discovery import TaskSpec, iter_task_specs, load_task_spec
from synth_rearc.shared.render import load_task_examples


def verify_examples(
    spec: TaskSpec,
    examples: list[dict],
    *,
    example_labels: Sequence[str] | None = None,
) -> dict[str, object]:
    if example_labels is not None and len(example_labels) != len(examples):
        raise ValueError("example_labels must match examples length")

    failures: list[str] = []
    for idx, example in enumerate(examples):
        label = example_labels[idx] if example_labels is not None else f"example {idx:02d}"
        if "input" not in example:
            failures.append(f"{label}: missing input")
            continue
        if "output" not in example:
            failures.append(f"{label}: missing output")
            continue
        formatted = format_example(example)
        try:
            actual = spec.verifier(formatted["input"])
        except Exception as exc:
            failures.append(f"{label}: {type(exc).__name__}: {exc}")
            continue
        if actual != formatted["output"]:
            failures.append(f"{label}: output mismatch")

    return {
        "task_id": spec.task_id,
        "total": len(examples),
        "passed": len(examples) - len(failures),
        "failures": failures,
    }


def verify_official_examples(spec: TaskSpec) -> dict[str, object]:
    examples = load_task_examples(spec.reference_task_path)
    return verify_examples(spec, examples)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Verify synthetic RE-ARC verifiers on official examples.")
    parser.add_argument("--task", help="Task id or task package name. Verifies all tasks if omitted.")
    parser.add_argument("--dataset", choices=("arc1", "arc2"))
    parser.add_argument("--split", choices=("training", "evaluation"))
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if (args.dataset is None) != (args.split is None):
        print("fail: --dataset and --split must be provided together")
        return 1
    try:
        specs = (
            [load_task_spec(args.task, dataset=args.dataset, split=args.split)]
            if args.task
            else list(iter_task_specs(dataset=args.dataset, split=args.split))
        )
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

        print(
            f"pass {spec.dataset}/{spec.split}/{spec.task_id}: "
            f"{result['passed']}/{result['total']} official examples passed"
        )

    return 0 if all_passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
