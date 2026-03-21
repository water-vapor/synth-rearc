from .generator import generate_c9680e90
from .verifier import verify_c9680e90


TASK_ID = "c9680e90"
generate = generate_c9680e90
verify = verify_c9680e90
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/c9680e90.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c9680e90",
    "verify",
    "verify_c9680e90",
]
