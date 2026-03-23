from .generator import generate_25c199f5
from .verifier import verify_25c199f5


TASK_ID = "25c199f5"
generate = generate_25c199f5
verify = verify_25c199f5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/25c199f5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_25c199f5",
    "verify",
    "verify_25c199f5",
]
