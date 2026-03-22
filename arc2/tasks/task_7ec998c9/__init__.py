from .generator import generate_7ec998c9
from .verifier import verify_7ec998c9


TASK_ID = "7ec998c9"
generate = generate_7ec998c9
verify = verify_7ec998c9
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7ec998c9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7ec998c9",
    "verify",
    "verify_7ec998c9",
]
