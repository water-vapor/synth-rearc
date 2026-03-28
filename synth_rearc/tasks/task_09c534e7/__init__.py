from .generator import generate_09c534e7
from .verifier import verify_09c534e7


TASK_ID = "09c534e7"
generate = generate_09c534e7
verify = verify_09c534e7
REFERENCE_TASK_PATH = "data/official/arc2/training/09c534e7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_09c534e7",
    "verify",
    "verify_09c534e7",
]
