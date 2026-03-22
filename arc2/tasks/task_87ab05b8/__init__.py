from .generator import generate_87ab05b8
from .verifier import verify_87ab05b8


TASK_ID = "87ab05b8"
generate = generate_87ab05b8
verify = verify_87ab05b8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/87ab05b8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_87ab05b8",
    "verify",
    "verify_87ab05b8",
]
