from .generator import generate_759f3fd3
from .verifier import verify_759f3fd3


TASK_ID = "759f3fd3"
generate = generate_759f3fd3
verify = verify_759f3fd3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/759f3fd3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_759f3fd3",
    "verify",
    "verify_759f3fd3",
]
