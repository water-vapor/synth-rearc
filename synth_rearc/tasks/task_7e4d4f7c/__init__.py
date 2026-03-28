from .generator import generate_7e4d4f7c
from .verifier import verify_7e4d4f7c


TASK_ID = "7e4d4f7c"
generate = generate_7e4d4f7c
verify = verify_7e4d4f7c
REFERENCE_TASK_PATH = "data/official/arc2/training/7e4d4f7c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7e4d4f7c",
    "verify",
    "verify_7e4d4f7c",
]
