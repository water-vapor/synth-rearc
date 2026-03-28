from .generator import generate_6a980be1
from .verifier import verify_6a980be1


TASK_ID = "6a980be1"
generate = generate_6a980be1
verify = verify_6a980be1
REFERENCE_TASK_PATH = "data/official/arc2/training/6a980be1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6a980be1",
    "verify",
    "verify_6a980be1",
]
