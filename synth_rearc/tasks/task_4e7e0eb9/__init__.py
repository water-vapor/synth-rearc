from .generator import generate_4e7e0eb9
from .verifier import verify_4e7e0eb9


TASK_ID = "4e7e0eb9"
generate = generate_4e7e0eb9
verify = verify_4e7e0eb9
REFERENCE_TASK_PATH = "data/official/arc2/training/4e7e0eb9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4e7e0eb9",
    "verify",
    "verify_4e7e0eb9",
]
