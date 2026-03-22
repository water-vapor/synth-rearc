from .generator import generate_7953d61e
from .verifier import verify_7953d61e


TASK_ID = "7953d61e"
generate = generate_7953d61e
verify = verify_7953d61e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7953d61e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7953d61e",
    "verify",
    "verify_7953d61e",
]
