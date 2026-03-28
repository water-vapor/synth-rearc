#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

TASK_LIST="${TASK_LIST:-data/task_lists/arc2_training_minus_arc1_task_ids.txt}"
DATASET="${DATASET:-arc2}"
SPLIT="${SPLIT:-training}"

if [[ ! -f "$TASK_LIST" ]]; then
  echo "Task list not found: $TASK_LIST" >&2
  exit 1
fi

while IFS= read -r task_id; do
  if [[ -z "$task_id" ]]; then
    continue
  fi
  python "$SCRIPT_DIR/synth_rearc_generate_task_cc.py" --dataset "$DATASET" --split "$SPLIT" "$task_id"
done < "$TASK_LIST"
