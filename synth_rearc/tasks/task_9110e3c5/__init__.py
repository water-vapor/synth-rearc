from .generator import generate_9110e3c5
from .verifier import verify_9110e3c5


TASK_ID = "9110e3c5"
generate = generate_9110e3c5
verify = verify_9110e3c5
REFERENCE_TASK_PATH = "data/official/arc2/training/9110e3c5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9110e3c5",
    "verify",
    "verify_9110e3c5",
]
