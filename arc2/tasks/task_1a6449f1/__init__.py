from .generator import generate_1a6449f1
from .verifier import verify_1a6449f1


TASK_ID = "1a6449f1"
generate = generate_1a6449f1
verify = verify_1a6449f1
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1a6449f1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1a6449f1",
    "verify",
    "verify_1a6449f1",
]
