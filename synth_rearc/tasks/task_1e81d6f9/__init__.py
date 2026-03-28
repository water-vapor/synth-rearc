from .generator import generate_1e81d6f9
from .verifier import verify_1e81d6f9


TASK_ID = "1e81d6f9"
generate = generate_1e81d6f9
verify = verify_1e81d6f9
REFERENCE_TASK_PATH = "data/official/arc2/training/1e81d6f9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1e81d6f9",
    "verify",
    "verify_1e81d6f9",
]
