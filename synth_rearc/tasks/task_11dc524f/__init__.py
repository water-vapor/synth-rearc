from .generator import generate_11dc524f
from .verifier import verify_11dc524f


TASK_ID = "11dc524f"
generate = generate_11dc524f
verify = verify_11dc524f
REFERENCE_TASK_PATH = "data/official/arc2/training/11dc524f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_11dc524f",
    "verify",
    "verify_11dc524f",
]
