from .generator import generate_817e6c09
from .verifier import verify_817e6c09


TASK_ID = "817e6c09"
generate = generate_817e6c09
verify = verify_817e6c09
REFERENCE_TASK_PATH = "data/official/arc2/training/817e6c09.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_817e6c09",
    "verify",
    "verify_817e6c09",
]
