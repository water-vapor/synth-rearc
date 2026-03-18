from .generator import generate_0b17323b
from .verifier import verify_0b17323b


TASK_ID = "0b17323b"
generate = generate_0b17323b
verify = verify_0b17323b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/0b17323b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0b17323b",
    "verify",
    "verify_0b17323b",
]
