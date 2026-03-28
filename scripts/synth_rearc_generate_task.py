#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
from pathlib import Path
from typing import Any

MODEL = "gpt-5.4"
REASONING_EFFORT = "xhigh"
IDLE_TIMEOUT_SECONDS = 1800.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the synthetic RE-ARC task-generation prompt for a single puzzle id."
    )
    parser.add_argument("puzzle_id", help="Puzzle id, for example 0a1d4ef5.")
    parser.add_argument("--dataset", choices=("arc1", "arc2"), required=True)
    parser.add_argument("--split", choices=("training", "evaluation"), required=True)
    return parser.parse_args()


def build_prompt(*, prompt_path: Path, dataset: str, split: str, puzzle_id: str) -> str:
    return (
        "Please do the task stated in "
        f"`{prompt_path}`, "
        f"where DATASET is `{dataset}`, SPLIT is `{split}`, and TASK_ID is `{puzzle_id}`."
    )


def save_payload(*, repo_root: Path, puzzle_id: str, payload: dict[str, Any]) -> None:
    logs_dir = repo_root / "logs"
    logs_dir.mkdir(exist_ok=True)
    with open(logs_dir / f"{puzzle_id}.json", "w") as fp:
        json.dump(payload, fp, indent=2)


async def run_codex_task(*, prompt: str, working_dir: Path) -> dict[str, Any]:
    from agents.extensions.experimental.codex import Codex, ThreadOptions, TurnOptions

    codex = Codex()
    thread = codex.start_thread(
        ThreadOptions(
            model=MODEL,
            model_reasoning_effort=REASONING_EFFORT,
            sandbox_mode="danger-full-access",
            working_directory=str(working_dir),
            skip_git_repo_check=True,
            network_access_enabled=True,
            web_search_mode="live",
            approval_policy="never",
        )
    )
    turn = await thread.run(
        prompt,
        TurnOptions(idle_timeout_seconds=IDLE_TIMEOUT_SECONDS),
    )
    return {
        "working_dir": str(working_dir),
        "prompt": prompt,
        "thread_id": thread.id,
        "codex_response": turn.final_response,
        "usage": turn.usage.as_dict() if turn.usage is not None else None,
    }


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[1]
    prompt_path = repo_root / "prompts" / "synth_rearc_task_generation.md"
    puzzle_id = args.puzzle_id
    task_dir = repo_root / "synth_rearc" / "tasks" / f"task_{puzzle_id}"

    if task_dir.exists():
        print(f"Task directory already exists: {task_dir}")
        return 0

    payload = asyncio.run(
        run_codex_task(
            prompt=build_prompt(
                prompt_path=prompt_path,
                dataset=args.dataset,
                split=args.split,
                puzzle_id=puzzle_id,
            ),
            working_dir=repo_root,
        )
    )
    payload["puzzle_id"] = puzzle_id
    payload["dataset"] = args.dataset
    payload["split"] = args.split
    payload["status"] = "completed"
    save_payload(repo_root=repo_root, puzzle_id=puzzle_id, payload=payload)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
