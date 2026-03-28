from .generator import generate_a09f6c25
from .verifier import verify_a09f6c25


TASK_ID = "a09f6c25"
generate = generate_a09f6c25
verify = verify_a09f6c25
REFERENCE_TASK_PATH = "data/official/arc2/training/a09f6c25.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a09f6c25",
    "verify",
    "verify_a09f6c25",
]
