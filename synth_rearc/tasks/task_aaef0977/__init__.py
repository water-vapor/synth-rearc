from .generator import generate_aaef0977
from .verifier import verify_aaef0977


TASK_ID = "aaef0977"
generate = generate_aaef0977
verify = verify_aaef0977
REFERENCE_TASK_PATH = "data/official/arc2/training/aaef0977.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_aaef0977",
    "verify",
    "verify_aaef0977",
]
