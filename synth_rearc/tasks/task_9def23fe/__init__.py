from .generator import generate_9def23fe
from .verifier import verify_9def23fe


TASK_ID = "9def23fe"
generate = generate_9def23fe
verify = verify_9def23fe
REFERENCE_TASK_PATH = "data/official/arc2/training/9def23fe.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9def23fe",
    "verify",
    "verify_9def23fe",
]
