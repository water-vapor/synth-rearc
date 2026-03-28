from .generator import generate_e69241bd
from .verifier import verify_e69241bd


TASK_ID = "e69241bd"
generate = generate_e69241bd
verify = verify_e69241bd
REFERENCE_TASK_PATH = "data/official/arc2/training/e69241bd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e69241bd",
    "verify",
    "verify_e69241bd",
]
