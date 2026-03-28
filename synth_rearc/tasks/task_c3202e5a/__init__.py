from .generator import generate_c3202e5a
from .verifier import verify_c3202e5a


TASK_ID = "c3202e5a"
generate = generate_c3202e5a
verify = verify_c3202e5a
REFERENCE_TASK_PATH = "data/official/arc2/training/c3202e5a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c3202e5a",
    "verify",
    "verify_c3202e5a",
]
