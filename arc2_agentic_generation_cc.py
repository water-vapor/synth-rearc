#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import subprocess
from pathlib import Path
from typing import Any

MODEL = "claude-opus-4-6"
REASONING_EFFORT = "high"
TIMEOUT_SECONDS = 1800.0
LOG_SUFFIX = "_cc"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the ARC2 task-generation prompt for a single puzzle id with Claude Code."
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
    with open(logs_dir / f"{puzzle_id}{LOG_SUFFIX}.json", "w") as fp:
        json.dump(payload, fp, indent=2)


def _parse_events(stdout: str) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for index, raw_line in enumerate(stdout.splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise RuntimeError(
                f"Claude Code emitted invalid JSON on line {index}: {raw_line!r}"
            ) from exc
    return events


def _find_event(events: list[dict[str, Any]], event_type: str) -> dict[str, Any] | None:
    for event in reversed(events):
        if event.get("type") == event_type:
            return event
    return None


def run_claude_code_task(*, prompt: str, working_dir: Path) -> dict[str, Any]:
    working_dir = working_dir.resolve()
    if not working_dir.is_dir():
        raise ValueError(f"working_dir does not exist or is not a directory: {working_dir}")

    command = [
        "claude",
        "-p",
        "--output-format",
        "stream-json",
        "--verbose",
        "--model",
        MODEL,
        "--effort",
        REASONING_EFFORT,
        "--dangerously-skip-permissions",
        "--no-session-persistence",
        prompt,
    ]
    completed = subprocess.run(
        command,
        cwd=working_dir,
        check=True,
        capture_output=True,
        text=True,
        timeout=TIMEOUT_SECONDS,
    )
    events = _parse_events(completed.stdout)
    init_event = _find_event(events, "system")
    result_event = _find_event(events, "result")
    if result_event is None:
        raise RuntimeError("Claude Code did not emit a result event.")

    final_response = result_event.get("result")
    session_id = result_event.get("session_id") or (init_event or {}).get("session_id")
    return {
        "working_dir": str(working_dir),
        "prompt": prompt,
        "agent": "claude_code",
        "session_id": session_id,
        "run_id": session_id,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "claude_response": final_response,
        "final_response": final_response,
        "conversation": [
            {
                "type": "user",
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
                "synthetic": True,
            },
            *events,
        ],
        "usage": result_event.get("usage"),
        "model_usage": result_event.get("modelUsage"),
        "total_cost_usd": result_event.get("total_cost_usd"),
    }


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parent
    puzzle_id = args.puzzle_id
    task_dir = repo_root / "arc2" / "tasks" / f"task_{puzzle_id}"

    if task_dir.exists():
        print(f"Task directory already exists: {task_dir}")
        return 0

    payload = run_claude_code_task(
        prompt=build_prompt(puzzle_id),
        working_dir=repo_root,
    )
    payload["puzzle_id"] = puzzle_id
    payload["status"] = "completed"
    save_payload(repo_root=repo_root, puzzle_id=puzzle_id, payload=payload)
    print(json.dumps(payload, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
