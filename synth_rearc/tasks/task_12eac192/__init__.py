from .generator import generate_12eac192
from .verifier import verify_12eac192


TASK_ID = "12eac192"
generate = generate_12eac192
verify = verify_12eac192
REFERENCE_TASK_PATH = "data/official/arc2/training/12eac192.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_12eac192",
    "verify",
    "verify_12eac192",
]
