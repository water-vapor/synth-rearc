from .generator import generate_22208ba4
from .verifier import verify_22208ba4


TASK_ID = "22208ba4"
generate = generate_22208ba4
verify = verify_22208ba4
REFERENCE_TASK_PATH = "data/official/arc2/training/22208ba4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_22208ba4",
    "verify",
    "verify_22208ba4",
]
