from .generator import generate_332202d5
from .verifier import verify_332202d5


TASK_ID = "332202d5"
generate = generate_332202d5
verify = verify_332202d5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/332202d5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_332202d5",
    "verify",
    "verify_332202d5",
]
