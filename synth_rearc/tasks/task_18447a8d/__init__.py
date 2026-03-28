from .generator import generate_18447a8d
from .verifier import verify_18447a8d


TASK_ID = "18447a8d"
generate = generate_18447a8d
verify = verify_18447a8d
REFERENCE_TASK_PATH = "data/official/arc2/training/18447a8d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_18447a8d",
    "verify",
    "verify_18447a8d",
]
