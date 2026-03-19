from .generator import generate_e9c9d9a1
from .verifier import verify_e9c9d9a1


TASK_ID = "e9c9d9a1"
generate = generate_e9c9d9a1
verify = verify_e9c9d9a1
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e9c9d9a1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e9c9d9a1",
    "verify",
    "verify_e9c9d9a1",
]
