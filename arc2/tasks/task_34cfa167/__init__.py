from .generator import generate_34cfa167
from .verifier import verify_34cfa167


TASK_ID = "34cfa167"
generate = generate_34cfa167
verify = verify_34cfa167
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/34cfa167.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_34cfa167",
    "verify",
    "verify_34cfa167",
]
