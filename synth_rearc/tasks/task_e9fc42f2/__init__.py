from .generator import generate_e9fc42f2
from .verifier import verify_e9fc42f2


TASK_ID = "e9fc42f2"
generate = generate_e9fc42f2
verify = verify_e9fc42f2
REFERENCE_TASK_PATH = "data/official/arc2/training/e9fc42f2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e9fc42f2",
    "verify",
    "verify_e9fc42f2",
]
