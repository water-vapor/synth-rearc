from .generator import generate_8e2edd66
from .verifier import verify_8e2edd66


TASK_ID = "8e2edd66"
generate = generate_8e2edd66
verify = verify_8e2edd66
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/8e2edd66.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8e2edd66",
    "verify",
    "verify_8e2edd66",
]
