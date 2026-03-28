from .generator import generate_5d2a5c43
from .verifier import verify_5d2a5c43


TASK_ID = "5d2a5c43"
generate = generate_5d2a5c43
verify = verify_5d2a5c43
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5d2a5c43.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5d2a5c43",
    "verify",
    "verify_5d2a5c43",
]
