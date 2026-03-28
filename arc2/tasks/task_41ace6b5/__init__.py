from .generator import generate_41ace6b5
from .verifier import verify_41ace6b5


TASK_ID = "41ace6b5"
generate = generate_41ace6b5
verify = verify_41ace6b5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/41ace6b5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_41ace6b5",
    "verify",
    "verify_41ace6b5",
]
