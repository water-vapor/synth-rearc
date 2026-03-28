from .generator import generate_7bb29440
from .verifier import verify_7bb29440


TASK_ID = "7bb29440"
generate = generate_7bb29440
verify = verify_7bb29440
REFERENCE_TASK_PATH = "data/official/arc2/training/7bb29440.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7bb29440",
    "verify",
    "verify_7bb29440",
]
