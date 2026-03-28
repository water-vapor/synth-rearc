from .generator import generate_e633a9e5
from .verifier import verify_e633a9e5


TASK_ID = "e633a9e5"
generate = generate_e633a9e5
verify = verify_e633a9e5
REFERENCE_TASK_PATH = "data/official/arc2/training/e633a9e5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e633a9e5",
    "verify",
    "verify_e633a9e5",
]
