from .generator import generate_753ea09b
from .verifier import verify_753ea09b


TASK_ID = "753ea09b"
generate = generate_753ea09b
verify = verify_753ea09b
REFERENCE_TASK_PATH = "data/official/arc2/training/753ea09b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_753ea09b",
    "verify",
    "verify_753ea09b",
]
