from .generator import generate_c6e1b8da
from .verifier import verify_c6e1b8da


TASK_ID = "c6e1b8da"
generate = generate_c6e1b8da
verify = verify_c6e1b8da
REFERENCE_TASK_PATH = "data/official/arc2/training/c6e1b8da.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c6e1b8da",
    "verify",
    "verify_c6e1b8da",
]
