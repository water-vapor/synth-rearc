from .generator import generate_3979b1a8
from .verifier import verify_3979b1a8


TASK_ID = "3979b1a8"
generate = generate_3979b1a8
verify = verify_3979b1a8
REFERENCE_TASK_PATH = "data/official/arc2/training/3979b1a8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3979b1a8",
    "verify",
    "verify_3979b1a8",
]
