from .generator import generate_18286ef8
from .verifier import verify_18286ef8


TASK_ID = "18286ef8"
generate = generate_18286ef8
verify = verify_18286ef8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/18286ef8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_18286ef8",
    "verify",
    "verify_18286ef8",
]
