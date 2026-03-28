from .generator import generate_58e15b12
from .verifier import verify_58e15b12


TASK_ID = "58e15b12"
generate = generate_58e15b12
verify = verify_58e15b12
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/58e15b12.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_58e15b12",
    "verify",
    "verify_58e15b12",
]
