from .generator import generate_0d87d2a6
from .verifier import verify_0d87d2a6


TASK_ID = "0d87d2a6"
generate = generate_0d87d2a6
verify = verify_0d87d2a6
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/0d87d2a6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0d87d2a6",
    "verify",
    "verify_0d87d2a6",
]
