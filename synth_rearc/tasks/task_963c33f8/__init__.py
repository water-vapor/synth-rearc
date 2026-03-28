from .generator import generate_963c33f8
from .verifier import verify_963c33f8


TASK_ID = "963c33f8"
generate = generate_963c33f8
verify = verify_963c33f8
REFERENCE_TASK_PATH = "data/official/arc2/training/963c33f8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_963c33f8",
    "verify",
    "verify_963c33f8",
]
