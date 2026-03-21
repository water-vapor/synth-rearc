from .generator import generate_9f5f939b
from .verifier import verify_9f5f939b


TASK_ID = "9f5f939b"
generate = generate_9f5f939b
verify = verify_9f5f939b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9f5f939b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9f5f939b",
    "verify",
    "verify_9f5f939b",
]
