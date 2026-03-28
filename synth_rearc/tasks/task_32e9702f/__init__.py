from .generator import generate_32e9702f
from .verifier import verify_32e9702f


TASK_ID = "32e9702f"
REFERENCE_TASK_PATH = "data/official/arc2/training/32e9702f.json"

generate = generate_32e9702f
verify = verify_32e9702f

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_32e9702f",
    "verify",
    "verify_32e9702f",
]
