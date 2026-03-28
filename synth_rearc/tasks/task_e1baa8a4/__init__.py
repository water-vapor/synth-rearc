from .generator import generate_e1baa8a4
from .verifier import verify_e1baa8a4


TASK_ID = "e1baa8a4"
generate = generate_e1baa8a4
verify = verify_e1baa8a4
REFERENCE_TASK_PATH = "data/official/arc2/training/e1baa8a4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e1baa8a4",
    "verify",
    "verify_e1baa8a4",
]
