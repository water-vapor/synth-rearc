from .generator import generate_3cd86f4f
from .verifier import verify_3cd86f4f


TASK_ID = "3cd86f4f"
generate = generate_3cd86f4f
verify = verify_3cd86f4f
REFERENCE_TASK_PATH = "data/official/arc2/training/3cd86f4f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3cd86f4f",
    "verify",
    "verify_3cd86f4f",
]
