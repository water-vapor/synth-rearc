from .generator import generate_27a77e38
from .verifier import verify_27a77e38


TASK_ID = "27a77e38"
generate = generate_27a77e38
verify = verify_27a77e38
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/27a77e38.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_27a77e38",
    "verify",
    "verify_27a77e38",
]
