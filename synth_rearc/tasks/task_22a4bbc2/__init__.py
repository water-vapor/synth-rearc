from .generator import generate_22a4bbc2
from .verifier import verify_22a4bbc2


TASK_ID = "22a4bbc2"
generate = generate_22a4bbc2
verify = verify_22a4bbc2
REFERENCE_TASK_PATH = "data/official/arc2/training/22a4bbc2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_22a4bbc2",
    "verify",
    "verify_22a4bbc2",
]
