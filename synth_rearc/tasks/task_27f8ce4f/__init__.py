from .generator import generate_27f8ce4f
from .verifier import verify_27f8ce4f


TASK_ID = "27f8ce4f"
generate = generate_27f8ce4f
verify = verify_27f8ce4f
REFERENCE_TASK_PATH = "data/official/arc2/training/27f8ce4f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_27f8ce4f",
    "verify",
    "verify_27f8ce4f",
]
