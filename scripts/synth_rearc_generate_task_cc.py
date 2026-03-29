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
        description="Run the synthetic RE-ARC task-generation prompt for a single puzzle id with Claude Code."
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


def run_claude_code_task(*, prompt: str, cwd: Path) -> dict[str, Any]:
    cwd = cwd.resolve()
    if not cwd.is_dir():
        raise ValueError(f"cwd does not exist or is not a directory: {cwd}")

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
        cwd=cwd,
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
    repo_root = Path(__file__).resolve().parents[1]
    prompt_path = repo_root / "prompts" / "synth_rearc_task_generation.md"
    puzzle_id = args.puzzle_id
    task_dir = repo_root / "synth_rearc" / "tasks" / f"task_{puzzle_id}"

    if task_dir.exists():
        print(f"Task directory already exists: {task_dir}")
        return 0

    payload = run_claude_code_task(
        prompt=build_prompt(
            prompt_path=prompt_path,
            dataset=args.dataset,
            split=args.split,
            puzzle_id=puzzle_id,
        ),
        cwd=repo_root,
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
