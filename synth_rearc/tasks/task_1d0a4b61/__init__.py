from .generator import generate_1d0a4b61
from .verifier import verify_1d0a4b61


TASK_ID = "1d0a4b61"
generate = generate_1d0a4b61
verify = verify_1d0a4b61
REFERENCE_TASK_PATH = "data/official/arc2/training/1d0a4b61.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1d0a4b61",
    "verify",
    "verify_1d0a4b61",
]
