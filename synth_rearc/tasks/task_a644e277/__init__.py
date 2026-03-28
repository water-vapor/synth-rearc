from .generator import generate_a644e277
from .verifier import verify_a644e277


TASK_ID = "a644e277"
generate = generate_a644e277
verify = verify_a644e277
REFERENCE_TASK_PATH = "data/official/arc2/training/a644e277.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a644e277",
    "verify",
    "verify_a644e277",
]
