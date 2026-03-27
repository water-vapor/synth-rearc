from .generator import generate_305b1341
from .verifier import verify_305b1341


TASK_ID = "305b1341"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/305b1341.json"

generate = generate_305b1341
verify = verify_305b1341

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_305b1341",
    "verify",
    "verify_305b1341",
]
