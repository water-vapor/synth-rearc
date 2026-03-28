from .generator import generate_14b8e18c
from .verifier import verify_14b8e18c


TASK_ID = "14b8e18c"
generate = generate_14b8e18c
verify = verify_14b8e18c
REFERENCE_TASK_PATH = "data/official/arc2/training/14b8e18c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_14b8e18c",
    "verify",
    "verify_14b8e18c",
]
