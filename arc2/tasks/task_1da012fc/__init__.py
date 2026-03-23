from .generator import generate_1da012fc
from .verifier import verify_1da012fc


TASK_ID = "1da012fc"
generate = generate_1da012fc
verify = verify_1da012fc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1da012fc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1da012fc",
    "verify",
    "verify_1da012fc",
]
