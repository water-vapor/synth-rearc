from .generator import generate_d4b1c2b1
from .verifier import verify_d4b1c2b1


TASK_ID = "d4b1c2b1"
generate = generate_d4b1c2b1
verify = verify_d4b1c2b1
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d4b1c2b1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d4b1c2b1",
    "verify",
    "verify_d4b1c2b1",
]
