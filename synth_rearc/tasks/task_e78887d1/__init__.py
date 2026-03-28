from .generator import generate_e78887d1
from .verifier import verify_e78887d1


TASK_ID = "e78887d1"
generate = generate_e78887d1
verify = verify_e78887d1
REFERENCE_TASK_PATH = "data/official/arc2/training/e78887d1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e78887d1",
    "verify",
    "verify_e78887d1",
]
