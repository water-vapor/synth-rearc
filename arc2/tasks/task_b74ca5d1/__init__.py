from .generator import generate_b74ca5d1
from .verifier import verify_b74ca5d1


TASK_ID = "b74ca5d1"
generate = generate_b74ca5d1
verify = verify_b74ca5d1
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b74ca5d1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b74ca5d1",
    "verify",
    "verify_b74ca5d1",
]
