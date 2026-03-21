from .generator import generate_bb52a14b
from .verifier import verify_bb52a14b


TASK_ID = "bb52a14b"
generate = generate_bb52a14b
verify = verify_bb52a14b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/bb52a14b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bb52a14b",
    "verify",
    "verify_bb52a14b",
]
