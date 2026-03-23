from .generator import generate_6d1d5c90
from .verifier import verify_6d1d5c90


TASK_ID = "6d1d5c90"
generate = generate_6d1d5c90
verify = verify_6d1d5c90
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/6d1d5c90.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6d1d5c90",
    "verify",
    "verify_6d1d5c90",
]
