from .generator import generate_0c9aba6e
from .verifier import verify_0c9aba6e


TASK_ID = "0c9aba6e"
generate = generate_0c9aba6e
verify = verify_0c9aba6e
REFERENCE_TASK_PATH = "data/official/arc2/training/0c9aba6e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0c9aba6e",
    "verify",
    "verify_0c9aba6e",
]
