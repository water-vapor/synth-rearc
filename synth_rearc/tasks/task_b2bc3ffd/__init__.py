from .generator import generate_b2bc3ffd
from .verifier import verify_b2bc3ffd


TASK_ID = "b2bc3ffd"
generate = generate_b2bc3ffd
verify = verify_b2bc3ffd
REFERENCE_TASK_PATH = "data/official/arc2/training/b2bc3ffd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b2bc3ffd",
    "verify",
    "verify_b2bc3ffd",
]
