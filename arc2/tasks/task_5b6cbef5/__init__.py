from .generator import generate_5b6cbef5
from .verifier import verify_5b6cbef5


TASK_ID = "5b6cbef5"
generate = generate_5b6cbef5
verify = verify_5b6cbef5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5b6cbef5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5b6cbef5",
    "verify",
    "verify_5b6cbef5",
]
