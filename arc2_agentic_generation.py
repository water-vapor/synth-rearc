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
        description="Run the ARC2 task-generation prompt for a single puzzle id."
    )
    parser.add_argument("puzzle_id", help="ARC2 puzzle id, for example 0a1d4ef5.")
    return parser.parse_args()


def build_prompt(puzzle_id: str) -> str:
    return (
        "Please do the task stated in "
        "`/home/vapor/projects/realm/re-arc-2/re-arc/arc2_generation_prompts.md`, "
        f"where the TASK_ID is `{puzzle_id}`."
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
    repo_root = Path(__file__).resolve().parent
    puzzle_id = args.puzzle_id
    task_dir = repo_root / "arc2" / "tasks" / f"task_{puzzle_id}"

    if task_dir.exists():
        print(f"Task directory already exists: {task_dir}")
        return 0

    payload = asyncio.run(
        run_codex_task(
            prompt=build_prompt(puzzle_id),
            working_dir=repo_root,
        )
    )
    payload["puzzle_id"] = puzzle_id
    payload["status"] = "completed"
    save_payload(repo_root=repo_root, puzzle_id=puzzle_id, payload=payload)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
