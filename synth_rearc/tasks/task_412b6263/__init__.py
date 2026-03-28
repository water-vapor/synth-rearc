from .generator import generate_412b6263
from .verifier import verify_412b6263


TASK_ID = "412b6263"
generate = generate_412b6263
verify = verify_412b6263
REFERENCE_TASK_PATH = "data/official/arc2/training/412b6263.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_412b6263",
    "verify",
    "verify_412b6263",
]
