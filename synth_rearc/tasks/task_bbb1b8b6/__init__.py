from .generator import generate_bbb1b8b6
from .verifier import verify_bbb1b8b6


TASK_ID = "bbb1b8b6"
generate = generate_bbb1b8b6
verify = verify_bbb1b8b6
REFERENCE_TASK_PATH = "data/official/arc2/training/bbb1b8b6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bbb1b8b6",
    "verify",
    "verify_bbb1b8b6",
]
