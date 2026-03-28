from .generator import generate_e3f79277
from .verifier import verify_e3f79277


TASK_ID = "e3f79277"
generate = generate_e3f79277
verify = verify_e3f79277
REFERENCE_TASK_PATH = "data/official/arc2/training/e3f79277.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e3f79277",
    "verify",
    "verify_e3f79277",
]
