#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from synth_rearc_codex_lib import run_codex_task_sync, save_payload

DATASET = "arc1"
SPLIT = "training"
LOG_SUFFIX = "_black_background_fix"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the synthetic RE-ARC black-background-fix prompt for a single ARC1 training puzzle id."
    )
    parser.add_argument("puzzle_id", help="Puzzle id, for example 0a1d4ef5.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    prompt_path = repo_root / "prompts" / "synth_rearc_black_background_fix.md"
    puzzle_id = args.puzzle_id
    task_dir = repo_root / "synth_rearc" / "tasks" / f"task_{puzzle_id}"

    if task_dir.exists():
        print(f"Task directory already exists: {task_dir}")
        return 0

    payload = run_codex_task_sync(
        prompt=f"Please do the task stated in `{prompt_path}`, where TASK_ID is `{puzzle_id}`.",
        working_dir=repo_root,
    )
    payload["puzzle_id"] = puzzle_id
    payload["dataset"] = DATASET
    payload["split"] = SPLIT
    payload["status"] = "completed"
    save_payload(
        repo_root=repo_root,
        log_stem=f"{puzzle_id}{LOG_SUFFIX}",
        payload=payload,
    )
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
