#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$SCRIPT_DIR"

TASK_LIST="arc2_training_minus_arc1_task_ids.txt"

if [[ ! -f "$TASK_LIST" ]]; then
  echo "Task list not found: $TASK_LIST" >&2
  exit 1
fi

while IFS= read -r task_id; do
  if [[ -z "$task_id" ]]; then
    continue
  fi
  python arc2_agentic_generation_cc.py "$task_id"
done < "$TASK_LIST"
