from .generator import generate_e9ac8c9e
from .verifier import verify_e9ac8c9e


TASK_ID = "e9ac8c9e"
generate = generate_e9ac8c9e
verify = verify_e9ac8c9e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e9ac8c9e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e9ac8c9e",
    "verify",
    "verify_e9ac8c9e",
]
