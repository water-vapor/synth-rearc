from .generator import generate_8dab14c2
from .verifier import verify_8dab14c2


TASK_ID = "8dab14c2"
generate = generate_8dab14c2
verify = verify_8dab14c2
REFERENCE_TASK_PATH = "data/official/arc2/training/8dab14c2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8dab14c2",
    "verify",
    "verify_8dab14c2",
]
