from .generator import generate_94414823
from .verifier import verify_94414823


TASK_ID = "94414823"
generate = generate_94414823
verify = verify_94414823
REFERENCE_TASK_PATH = "data/official/arc2/training/94414823.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_94414823",
    "verify",
    "verify_94414823",
]
