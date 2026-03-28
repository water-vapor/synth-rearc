from .generator import generate_252143c9
from .verifier import verify_252143c9


TASK_ID = "252143c9"
generate = generate_252143c9
verify = verify_252143c9
REFERENCE_TASK_PATH = "data/official/arc2/training/252143c9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_252143c9",
    "verify",
    "verify_252143c9",
]
