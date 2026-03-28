from .generator import generate_c658a4bd
from .verifier import verify_c658a4bd


TASK_ID = "c658a4bd"
generate = generate_c658a4bd
verify = verify_c658a4bd
REFERENCE_TASK_PATH = "data/official/arc2/training/c658a4bd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c658a4bd",
    "verify",
    "verify_c658a4bd",
]
