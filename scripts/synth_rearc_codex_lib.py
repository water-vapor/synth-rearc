#!/usr/bin/env python3
from __future__ import annotations

import asyncio
import json
from pathlib import Path
from typing import Any

MODEL = "gpt-5.4"
REASONING_EFFORT = "xhigh"
IDLE_TIMEOUT_SECONDS = 1800.0


def save_payload(*, repo_root: Path, log_stem: str, payload: dict[str, Any]) -> None:
    logs_dir = repo_root / "logs"
    logs_dir.mkdir(exist_ok=True)
    with open(logs_dir / f"{log_stem}.json", "w") as fp:
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


def run_codex_task_sync(*, prompt: str, working_dir: Path) -> dict[str, Any]:
    return asyncio.run(run_codex_task(prompt=prompt, working_dir=working_dir))
