#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from synth_rearc_codex_lib import run_codex_task_sync, save_payload


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the synthetic RE-ARC task-generation prompt for a single puzzle id."
    )
    parser.add_argument("puzzle_id", help="Puzzle id, for example 0a1d4ef5.")
    parser.add_argument("--dataset", choices=("arc1", "arc2"), required=True)
    parser.add_argument("--split", choices=("training", "evaluation"), required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    prompt_path = repo_root / "prompts" / "synth_rearc_task_generation.md"
    puzzle_id = args.puzzle_id
    task_dir = repo_root / "synth_rearc" / "tasks" / f"task_{puzzle_id}"

    if task_dir.exists():
        print(f"Task directory already exists: {task_dir}")
        return 0

    payload = run_codex_task_sync(
        prompt=(
            "Please do the task stated in "
            f"`{prompt_path}`, "
            f"where DATASET is `{args.dataset}`, SPLIT is `{args.split}`, and TASK_ID is `{puzzle_id}`."
        ),
        cwd=repo_root,
    )
    payload["puzzle_id"] = puzzle_id
    payload["dataset"] = args.dataset
    payload["split"] = args.split
    payload["status"] = "completed"
    save_payload(repo_root=repo_root, log_stem=puzzle_id, payload=payload)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
