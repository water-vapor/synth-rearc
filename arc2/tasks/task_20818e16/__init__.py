from .generator import generate_20818e16
from .verifier import verify_20818e16


TASK_ID = "20818e16"
generate = generate_20818e16
verify = verify_20818e16
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/20818e16.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_20818e16",
    "verify",
    "verify_20818e16",
]
