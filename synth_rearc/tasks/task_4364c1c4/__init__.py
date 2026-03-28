from .generator import generate_4364c1c4
from .verifier import verify_4364c1c4


TASK_ID = "4364c1c4"
generate = generate_4364c1c4
verify = verify_4364c1c4
REFERENCE_TASK_PATH = "data/official/arc2/training/4364c1c4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4364c1c4",
    "verify",
    "verify_4364c1c4",
]
