from .generator import generate_66f2d22f
from .verifier import verify_66f2d22f


TASK_ID = "66f2d22f"
generate = generate_66f2d22f
verify = verify_66f2d22f
REFERENCE_TASK_PATH = "data/official/arc2/training/66f2d22f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_66f2d22f",
    "verify",
    "verify_66f2d22f",
]
