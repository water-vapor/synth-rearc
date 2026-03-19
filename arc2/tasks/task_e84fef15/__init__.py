from .generator import generate_e84fef15
from .verifier import verify_e84fef15


TASK_ID = "e84fef15"
generate = generate_e84fef15
verify = verify_e84fef15
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e84fef15.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e84fef15",
    "verify",
    "verify_e84fef15",
]
