from .generator import generate_c7d4e6ad
from .verifier import verify_c7d4e6ad


TASK_ID = "c7d4e6ad"
generate = generate_c7d4e6ad
verify = verify_c7d4e6ad
REFERENCE_TASK_PATH = "data/official/arc2/training/c7d4e6ad.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c7d4e6ad",
    "verify",
    "verify_c7d4e6ad",
]
