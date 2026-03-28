from .generator import generate_a1aa0c1e
from .verifier import verify_a1aa0c1e


TASK_ID = "a1aa0c1e"
generate = generate_a1aa0c1e
verify = verify_a1aa0c1e
REFERENCE_TASK_PATH = "data/official/arc2/training/a1aa0c1e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a1aa0c1e",
    "verify",
    "verify_a1aa0c1e",
]
