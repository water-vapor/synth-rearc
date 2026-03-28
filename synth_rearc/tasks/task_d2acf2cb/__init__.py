from .generator import generate_d2acf2cb
from .verifier import verify_d2acf2cb


TASK_ID = "d2acf2cb"
generate = generate_d2acf2cb
verify = verify_d2acf2cb
REFERENCE_TASK_PATH = "data/official/arc2/training/d2acf2cb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d2acf2cb",
    "verify",
    "verify_d2acf2cb",
]
