from .generator import generate_ecb67b6d
from .verifier import verify_ecb67b6d


TASK_ID = "ecb67b6d"
generate = generate_ecb67b6d
verify = verify_ecb67b6d
REFERENCE_TASK_PATH = "data/official/arc2/training/ecb67b6d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ecb67b6d",
    "verify",
    "verify_ecb67b6d",
]
