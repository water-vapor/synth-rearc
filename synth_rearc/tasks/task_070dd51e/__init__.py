from .generator import generate_070dd51e
from .verifier import verify_070dd51e


TASK_ID = "070dd51e"
generate = generate_070dd51e
verify = verify_070dd51e
REFERENCE_TASK_PATH = "data/official/arc2/training/070dd51e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_070dd51e",
    "verify",
    "verify_070dd51e",
]
