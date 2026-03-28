from .generator import generate_0c786b71
from .verifier import verify_0c786b71


TASK_ID = "0c786b71"
generate = generate_0c786b71
verify = verify_0c786b71
REFERENCE_TASK_PATH = "data/official/arc2/training/0c786b71.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0c786b71",
    "verify",
    "verify_0c786b71",
]
