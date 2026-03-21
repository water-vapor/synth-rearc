from .generator import generate_9ddd00f0
from .verifier import verify_9ddd00f0


TASK_ID = "9ddd00f0"
generate = generate_9ddd00f0
verify = verify_9ddd00f0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9ddd00f0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9ddd00f0",
    "verify",
    "verify_9ddd00f0",
]
