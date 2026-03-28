#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
cd "$REPO_ROOT"

TASK_LIST="data/task_lists/arc1_training_task_ids.txt"

if [[ ! -f "$TASK_LIST" ]]; then
  echo "Task list not found: $TASK_LIST" >&2
  exit 1
fi

START=${1:-1}
END=${2:-$(wc -l < "$TASK_LIST")}
TOTAL=$((END - START + 1))
DONE=0

sed -n "${START},${END}p" "$TASK_LIST" | while IFS= read -r task_id; do
  if [[ -z "$task_id" ]]; then
    continue
  fi
  python "$SCRIPT_DIR/synth_rearc_black_background_fix_task.py" "$task_id"
  DONE=$((DONE + 1))
  echo "$DONE/$TOTAL"
done
