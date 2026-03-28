from .generator import generate_e9bb6954
from .verifier import verify_e9bb6954


TASK_ID = "e9bb6954"
generate = generate_e9bb6954
verify = verify_e9bb6954
REFERENCE_TASK_PATH = "data/official/arc2/training/e9bb6954.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e9bb6954",
    "verify",
    "verify_e9bb6954",
]
