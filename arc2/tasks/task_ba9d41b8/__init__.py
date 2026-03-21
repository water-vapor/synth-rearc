from .generator import generate_ba9d41b8
from .verifier import verify_ba9d41b8


TASK_ID = "ba9d41b8"
generate = generate_ba9d41b8
verify = verify_ba9d41b8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ba9d41b8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ba9d41b8",
    "verify",
    "verify_ba9d41b8",
]
