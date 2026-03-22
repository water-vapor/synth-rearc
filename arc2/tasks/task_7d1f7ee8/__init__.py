from .generator import generate_7d1f7ee8
from .verifier import verify_7d1f7ee8


TASK_ID = "7d1f7ee8"
generate = generate_7d1f7ee8
verify = verify_7d1f7ee8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7d1f7ee8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7d1f7ee8",
    "verify",
    "verify_7d1f7ee8",
]
