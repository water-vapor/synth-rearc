from .generator import generate_5adee1b2
from .verifier import verify_5adee1b2


TASK_ID = "5adee1b2"
generate = generate_5adee1b2
verify = verify_5adee1b2
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5adee1b2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5adee1b2",
    "verify",
    "verify_5adee1b2",
]
