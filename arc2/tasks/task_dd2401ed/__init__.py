from .generator import generate_dd2401ed
from .verifier import verify_dd2401ed


TASK_ID = "dd2401ed"
generate = generate_dd2401ed
verify = verify_dd2401ed
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/dd2401ed.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dd2401ed",
    "verify",
    "verify_dd2401ed",
]
