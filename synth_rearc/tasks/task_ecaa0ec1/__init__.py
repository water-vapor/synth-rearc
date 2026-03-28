from .generator import generate_ecaa0ec1
from .verifier import verify_ecaa0ec1


TASK_ID = "ecaa0ec1"
generate = generate_ecaa0ec1
verify = verify_ecaa0ec1
REFERENCE_TASK_PATH = "data/official/arc2/training/ecaa0ec1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ecaa0ec1",
    "verify",
    "verify_ecaa0ec1",
]
