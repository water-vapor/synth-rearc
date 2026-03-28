from .generator import generate_58c02a16
from .verifier import verify_58c02a16


TASK_ID = "58c02a16"
generate = generate_58c02a16
verify = verify_58c02a16
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/58c02a16.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_58c02a16",
    "verify",
    "verify_58c02a16",
]
