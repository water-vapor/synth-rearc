from .generator import generate_6e4f6532
from .verifier import verify_6e4f6532


TASK_ID = "6e4f6532"
generate = generate_6e4f6532
verify = verify_6e4f6532
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/6e4f6532.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6e4f6532",
    "verify",
    "verify_6e4f6532",
]
