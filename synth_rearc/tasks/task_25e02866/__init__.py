from .generator import generate_25e02866
from .verifier import verify_25e02866


TASK_ID = "25e02866"
generate = generate_25e02866
verify = verify_25e02866
REFERENCE_TASK_PATH = "data/official/arc2/training/25e02866.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_25e02866",
    "verify",
    "verify_25e02866",
]
