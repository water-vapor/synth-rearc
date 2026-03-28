from .generator import generate_414297c0
from .verifier import verify_414297c0


TASK_ID = "414297c0"
generate = generate_414297c0
verify = verify_414297c0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/414297c0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_414297c0",
    "verify",
    "verify_414297c0",
]
