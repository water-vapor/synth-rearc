from .generator import generate_692cd3b6
from .verifier import verify_692cd3b6


TASK_ID = "692cd3b6"
generate = generate_692cd3b6
verify = verify_692cd3b6
REFERENCE_TASK_PATH = "data/official/arc2/training/692cd3b6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_692cd3b6",
    "verify",
    "verify_692cd3b6",
]
