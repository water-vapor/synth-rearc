from .generator import generate_d6542281
from .verifier import verify_d6542281


TASK_ID = "d6542281"
generate = generate_d6542281
verify = verify_d6542281
REFERENCE_TASK_PATH = "data/official/arc2/training/d6542281.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d6542281",
    "verify",
    "verify_d6542281",
]
