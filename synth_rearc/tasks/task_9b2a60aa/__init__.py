from .generator import generate_9b2a60aa
from .verifier import verify_9b2a60aa


TASK_ID = "9b2a60aa"
REFERENCE_TASK_PATH = "data/official/arc2/training/9b2a60aa.json"

generate = generate_9b2a60aa
verify = verify_9b2a60aa

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9b2a60aa",
    "verify",
    "verify_9b2a60aa",
]
