from .generator import generate_78e78cff
from .verifier import verify_78e78cff


TASK_ID = "78e78cff"
generate = generate_78e78cff
verify = verify_78e78cff
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/78e78cff.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_78e78cff",
    "verify",
    "verify_78e78cff",
]
