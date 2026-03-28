from .generator import generate_6350f1f4
from .verifier import verify_6350f1f4


TASK_ID = "6350f1f4"
generate = generate_6350f1f4
verify = verify_6350f1f4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/6350f1f4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6350f1f4",
    "verify",
    "verify_6350f1f4",
]
