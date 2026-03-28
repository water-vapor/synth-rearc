from .generator import generate_992798f6
from .verifier import verify_992798f6


TASK_ID = "992798f6"
generate = generate_992798f6
verify = verify_992798f6
REFERENCE_TASK_PATH = "data/official/arc2/training/992798f6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_992798f6",
    "verify",
    "verify_992798f6",
]
