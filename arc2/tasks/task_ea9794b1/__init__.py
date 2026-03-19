from .generator import generate_ea9794b1
from .verifier import verify_ea9794b1


TASK_ID = "ea9794b1"
generate = generate_ea9794b1
verify = verify_ea9794b1
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ea9794b1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ea9794b1",
    "verify",
    "verify_ea9794b1",
]
