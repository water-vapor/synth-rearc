from .generator import generate_8886d717
from .verifier import verify_8886d717


TASK_ID = "8886d717"
generate = generate_8886d717
verify = verify_8886d717
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/8886d717.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8886d717",
    "verify",
    "verify_8886d717",
]
