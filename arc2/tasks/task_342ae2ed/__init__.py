from .generator import generate_342ae2ed
from .verifier import verify_342ae2ed


TASK_ID = "342ae2ed"
generate = generate_342ae2ed
verify = verify_342ae2ed
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/342ae2ed.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_342ae2ed",
    "verify",
    "verify_342ae2ed",
]
