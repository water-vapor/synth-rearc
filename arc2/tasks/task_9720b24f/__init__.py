from .generator import generate_9720b24f
from .verifier import verify_9720b24f


TASK_ID = "9720b24f"
generate = generate_9720b24f
verify = verify_9720b24f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9720b24f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9720b24f",
    "verify",
    "verify_9720b24f",
]
