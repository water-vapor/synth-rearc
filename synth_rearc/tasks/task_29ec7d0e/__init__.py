from .generator import generate_29ec7d0e
from .verifier import verify_29ec7d0e


TASK_ID = "29ec7d0e"
REFERENCE_TASK_PATH = "data/official/arc1/training/29ec7d0e.json"

generate = generate_29ec7d0e
verify = verify_29ec7d0e

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_29ec7d0e",
    "verify",
    "verify_29ec7d0e",
]
