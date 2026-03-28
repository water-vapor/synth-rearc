from .generator import generate_90347967
from .verifier import verify_90347967


TASK_ID = "90347967"
generate = generate_90347967
verify = verify_90347967
REFERENCE_TASK_PATH = "data/official/arc2/training/90347967.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_90347967",
    "verify",
    "verify_90347967",
]
