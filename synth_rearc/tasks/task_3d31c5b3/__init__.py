from .generator import generate_3d31c5b3
from .verifier import verify_3d31c5b3


TASK_ID = "3d31c5b3"
generate = generate_3d31c5b3
verify = verify_3d31c5b3
REFERENCE_TASK_PATH = "data/official/arc2/training/3d31c5b3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3d31c5b3",
    "verify",
    "verify_3d31c5b3",
]
