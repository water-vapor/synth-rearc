from .generator import generate_9b5080bb
from .verifier import verify_9b5080bb


TASK_ID = "9b5080bb"
generate = generate_9b5080bb
verify = verify_9b5080bb
REFERENCE_TASK_PATH = "data/official/arc2/training/9b5080bb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9b5080bb",
    "verify",
    "verify_9b5080bb",
]
