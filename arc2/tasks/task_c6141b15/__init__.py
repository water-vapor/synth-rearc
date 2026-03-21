from .generator import generate_c6141b15
from .verifier import verify_c6141b15


TASK_ID = "c6141b15"
generate = generate_c6141b15
verify = verify_c6141b15
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/c6141b15.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c6141b15",
    "verify",
    "verify_c6141b15",
]
