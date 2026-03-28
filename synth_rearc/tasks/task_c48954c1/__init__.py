from .generator import generate_c48954c1
from .verifier import verify_c48954c1


TASK_ID = "c48954c1"
generate = generate_c48954c1
verify = verify_c48954c1
REFERENCE_TASK_PATH = "data/official/arc2/training/c48954c1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c48954c1",
    "verify",
    "verify_c48954c1",
]
