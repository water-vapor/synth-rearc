from .generator import generate_da2b0fe3
from .verifier import verify_da2b0fe3


TASK_ID = "da2b0fe3"
generate = generate_da2b0fe3
verify = verify_da2b0fe3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/da2b0fe3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_da2b0fe3",
    "verify",
    "verify_da2b0fe3",
]
