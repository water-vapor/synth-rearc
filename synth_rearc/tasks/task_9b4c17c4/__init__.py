from .generator import generate_9b4c17c4
from .verifier import verify_9b4c17c4


TASK_ID = "9b4c17c4"
generate = generate_9b4c17c4
verify = verify_9b4c17c4
REFERENCE_TASK_PATH = "data/official/arc2/training/9b4c17c4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9b4c17c4",
    "verify",
    "verify_9b4c17c4",
]
