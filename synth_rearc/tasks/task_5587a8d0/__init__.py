from .generator import generate_5587a8d0
from .verifier import verify_5587a8d0


TASK_ID = "5587a8d0"
generate = generate_5587a8d0
verify = verify_5587a8d0
REFERENCE_TASK_PATH = "data/official/arc2/training/5587a8d0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5587a8d0",
    "verify",
    "verify_5587a8d0",
]
