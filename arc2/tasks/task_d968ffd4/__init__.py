from .generator import generate_d968ffd4
from .verifier import verify_d968ffd4


TASK_ID = "d968ffd4"
generate = generate_d968ffd4
verify = verify_d968ffd4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d968ffd4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d968ffd4",
    "verify",
    "verify_d968ffd4",
]
