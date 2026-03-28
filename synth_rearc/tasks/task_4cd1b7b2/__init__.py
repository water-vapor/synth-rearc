from .generator import generate_4cd1b7b2
from .verifier import verify_4cd1b7b2


TASK_ID = "4cd1b7b2"
generate = generate_4cd1b7b2
verify = verify_4cd1b7b2
REFERENCE_TASK_PATH = "data/official/arc2/training/4cd1b7b2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4cd1b7b2",
    "verify",
    "verify_4cd1b7b2",
]
