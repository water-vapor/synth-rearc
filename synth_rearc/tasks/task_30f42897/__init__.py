from .generator import generate_30f42897
from .verifier import verify_30f42897


TASK_ID = "30f42897"
generate = generate_30f42897
verify = verify_30f42897
REFERENCE_TASK_PATH = "data/official/arc2/training/30f42897.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_30f42897",
    "verify",
    "verify_30f42897",
]
