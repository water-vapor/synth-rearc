from .generator import generate_6165ea8f
from .verifier import verify_6165ea8f


TASK_ID = "6165ea8f"
generate = generate_6165ea8f
verify = verify_6165ea8f
REFERENCE_TASK_PATH = "data/official/arc2/training/6165ea8f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6165ea8f",
    "verify",
    "verify_6165ea8f",
]
