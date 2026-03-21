from .generator import generate_b1fc8b8e
from .verifier import verify_b1fc8b8e


TASK_ID = "b1fc8b8e"
generate = generate_b1fc8b8e
verify = verify_b1fc8b8e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b1fc8b8e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b1fc8b8e",
    "verify",
    "verify_b1fc8b8e",
]
