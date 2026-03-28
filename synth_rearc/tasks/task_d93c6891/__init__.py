from .generator import generate_d93c6891
from .verifier import verify_d93c6891


TASK_ID = "d93c6891"
generate = generate_d93c6891
verify = verify_d93c6891
REFERENCE_TASK_PATH = "data/official/arc2/training/d93c6891.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d93c6891",
    "verify",
    "verify_d93c6891",
]
