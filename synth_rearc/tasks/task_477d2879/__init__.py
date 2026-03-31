from .generator import generate_477d2879
from .verifier import verify_477d2879


TASK_ID = "477d2879"
generate = generate_477d2879
verify = verify_477d2879
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/477d2879.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_477d2879",
    "verify",
    "verify_477d2879",
]
