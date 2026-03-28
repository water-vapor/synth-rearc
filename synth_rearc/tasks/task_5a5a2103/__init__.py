from .generator import generate_5a5a2103
from .verifier import verify_5a5a2103


TASK_ID = "5a5a2103"
generate = generate_5a5a2103
verify = verify_5a5a2103
REFERENCE_TASK_PATH = "data/official/arc2/training/5a5a2103.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5a5a2103",
    "verify",
    "verify_5a5a2103",
]
