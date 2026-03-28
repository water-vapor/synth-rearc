from .generator import generate_ad38a9d0
from .verifier import verify_ad38a9d0


TASK_ID = "ad38a9d0"
generate = generate_ad38a9d0
verify = verify_ad38a9d0
REFERENCE_TASK_PATH = "data/official/arc2/training/ad38a9d0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ad38a9d0",
    "verify",
    "verify_ad38a9d0",
]
