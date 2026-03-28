from .generator import generate_396d80d7
from .verifier import verify_396d80d7


TASK_ID = "396d80d7"
generate = generate_396d80d7
verify = verify_396d80d7
REFERENCE_TASK_PATH = "data/official/arc2/training/396d80d7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_396d80d7",
    "verify",
    "verify_396d80d7",
]
