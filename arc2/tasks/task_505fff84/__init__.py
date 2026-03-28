from .generator import generate_505fff84
from .verifier import verify_505fff84


TASK_ID = "505fff84"
generate = generate_505fff84
verify = verify_505fff84
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/505fff84.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_505fff84",
    "verify",
    "verify_505fff84",
]
