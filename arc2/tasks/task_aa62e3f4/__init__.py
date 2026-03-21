from .generator import generate_aa62e3f4
from .verifier import verify_aa62e3f4


TASK_ID = "aa62e3f4"
generate = generate_aa62e3f4
verify = verify_aa62e3f4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/aa62e3f4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_aa62e3f4",
    "verify",
    "verify_aa62e3f4",
]
