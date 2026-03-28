from .generator import generate_3ad05f52
from .verifier import verify_3ad05f52


TASK_ID = "3ad05f52"
generate = generate_3ad05f52
verify = verify_3ad05f52
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/3ad05f52.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3ad05f52",
    "verify",
    "verify_3ad05f52",
]
