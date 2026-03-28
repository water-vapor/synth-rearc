from .generator import generate_551d5bf1
from .verifier import verify_551d5bf1


TASK_ID = "551d5bf1"
generate = generate_551d5bf1
verify = verify_551d5bf1
REFERENCE_TASK_PATH = "data/official/arc2/training/551d5bf1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_551d5bf1",
    "verify",
    "verify_551d5bf1",
]
