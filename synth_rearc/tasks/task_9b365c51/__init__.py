from .generator import generate_9b365c51
from .verifier import verify_9b365c51


TASK_ID = "9b365c51"
generate = generate_9b365c51
verify = verify_9b365c51
REFERENCE_TASK_PATH = "data/official/arc2/training/9b365c51.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9b365c51",
    "verify",
    "verify_9b365c51",
]
