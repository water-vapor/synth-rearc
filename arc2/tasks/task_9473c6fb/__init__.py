from .generator import generate_9473c6fb
from .verifier import verify_9473c6fb


TASK_ID = "9473c6fb"
generate = generate_9473c6fb
verify = verify_9473c6fb
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9473c6fb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9473c6fb",
    "verify",
    "verify_9473c6fb",
]
