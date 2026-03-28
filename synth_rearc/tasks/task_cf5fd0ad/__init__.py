from .generator import generate_cf5fd0ad
from .verifier import verify_cf5fd0ad


TASK_ID = "cf5fd0ad"
generate = generate_cf5fd0ad
verify = verify_cf5fd0ad
REFERENCE_TASK_PATH = "data/official/arc2/training/cf5fd0ad.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cf5fd0ad",
    "verify",
    "verify_cf5fd0ad",
]
