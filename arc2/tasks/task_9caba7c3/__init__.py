from .generator import generate_9caba7c3
from .verifier import verify_9caba7c3


TASK_ID = "9caba7c3"
generate = generate_9caba7c3
verify = verify_9caba7c3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9caba7c3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9caba7c3",
    "verify",
    "verify_9caba7c3",
]
