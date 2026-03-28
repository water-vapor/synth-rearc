from .generator import generate_5034a0b5
from .verifier import verify_5034a0b5


TASK_ID = "5034a0b5"
generate = generate_5034a0b5
verify = verify_5034a0b5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5034a0b5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5034a0b5",
    "verify",
    "verify_5034a0b5",
]
