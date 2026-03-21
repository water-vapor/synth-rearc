from .generator import generate_9a4bb226
from .verifier import verify_9a4bb226


TASK_ID = "9a4bb226"
generate = generate_9a4bb226
verify = verify_9a4bb226
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9a4bb226.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9a4bb226",
    "verify",
    "verify_9a4bb226",
]
