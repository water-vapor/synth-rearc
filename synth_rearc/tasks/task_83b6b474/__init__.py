from .generator import generate_83b6b474
from .verifier import verify_83b6b474


TASK_ID = "83b6b474"
generate = generate_83b6b474
verify = verify_83b6b474
REFERENCE_TASK_PATH = "data/official/arc2/training/83b6b474.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_83b6b474",
    "verify",
    "verify_83b6b474",
]
