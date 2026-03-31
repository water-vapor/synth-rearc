from .generator import generate_58490d8a
from .verifier import verify_58490d8a


TASK_ID = "58490d8a"
generate = generate_58490d8a
verify = verify_58490d8a
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/58490d8a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_58490d8a",
    "verify",
    "verify_58490d8a",
]
