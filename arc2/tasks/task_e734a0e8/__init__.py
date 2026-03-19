from .generator import generate_e734a0e8
from .verifier import verify_e734a0e8


TASK_ID = "e734a0e8"
generate = generate_e734a0e8
verify = verify_e734a0e8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e734a0e8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e734a0e8",
    "verify",
    "verify_e734a0e8",
]
