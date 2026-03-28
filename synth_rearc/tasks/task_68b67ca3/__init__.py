from .generator import generate_68b67ca3
from .verifier import verify_68b67ca3


TASK_ID = "68b67ca3"
generate = generate_68b67ca3
verify = verify_68b67ca3
REFERENCE_TASK_PATH = "data/official/arc2/training/68b67ca3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_68b67ca3",
    "verify",
    "verify_68b67ca3",
]
