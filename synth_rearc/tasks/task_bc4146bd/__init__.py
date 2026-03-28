from .generator import generate_bc4146bd
from .verifier import verify_bc4146bd


TASK_ID = "bc4146bd"
generate = generate_bc4146bd
verify = verify_bc4146bd
REFERENCE_TASK_PATH = "data/official/arc2/training/bc4146bd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bc4146bd",
    "verify",
    "verify_bc4146bd",
]
