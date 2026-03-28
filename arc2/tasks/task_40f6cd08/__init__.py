from .generator import generate_40f6cd08
from .verifier import verify_40f6cd08


TASK_ID = "40f6cd08"
generate = generate_40f6cd08
verify = verify_40f6cd08
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/40f6cd08.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_40f6cd08",
    "verify",
    "verify_40f6cd08",
]
