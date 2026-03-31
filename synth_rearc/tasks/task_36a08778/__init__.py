from .generator import generate_36a08778
from .verifier import verify_36a08778


TASK_ID = "36a08778"
generate = generate_36a08778
verify = verify_36a08778
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/36a08778.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_36a08778",
    "verify",
    "verify_36a08778",
]
