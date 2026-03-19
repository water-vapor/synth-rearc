from .generator import generate_e048c9ed
from .verifier import verify_e048c9ed


TASK_ID = "e048c9ed"
generate = generate_e048c9ed
verify = verify_e048c9ed
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e048c9ed.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e048c9ed",
    "verify",
    "verify_e048c9ed",
]
