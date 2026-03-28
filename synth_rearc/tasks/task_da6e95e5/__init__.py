from .generator import generate_da6e95e5
from .verifier import verify_da6e95e5


TASK_ID = "da6e95e5"
generate = generate_da6e95e5
verify = verify_da6e95e5
REFERENCE_TASK_PATH = "data/official/arc2/training/da6e95e5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_da6e95e5",
    "verify",
    "verify_da6e95e5",
]
