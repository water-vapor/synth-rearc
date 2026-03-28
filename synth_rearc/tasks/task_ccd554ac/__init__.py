from .generator import generate_ccd554ac
from .verifier import verify_ccd554ac


TASK_ID = "ccd554ac"
generate = generate_ccd554ac
verify = verify_ccd554ac
REFERENCE_TASK_PATH = "data/official/arc2/training/ccd554ac.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ccd554ac",
    "verify",
    "verify_ccd554ac",
]
