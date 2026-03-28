from .generator import generate_212895b5
from .verifier import verify_212895b5


TASK_ID = "212895b5"
generate = generate_212895b5
verify = verify_212895b5
REFERENCE_TASK_PATH = "data/official/arc2/training/212895b5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_212895b5",
    "verify",
    "verify_212895b5",
]
