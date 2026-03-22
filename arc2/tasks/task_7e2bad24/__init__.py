from .generator import generate_7e2bad24
from .verifier import verify_7e2bad24


TASK_ID = "7e2bad24"
generate = generate_7e2bad24
verify = verify_7e2bad24
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7e2bad24.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7e2bad24",
    "verify",
    "verify_7e2bad24",
]
