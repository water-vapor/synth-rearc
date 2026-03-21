from .generator import generate_b7f8a4d8
from .verifier import verify_b7f8a4d8


TASK_ID = "b7f8a4d8"
generate = generate_b7f8a4d8
verify = verify_b7f8a4d8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b7f8a4d8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b7f8a4d8",
    "verify",
    "verify_b7f8a4d8",
]
