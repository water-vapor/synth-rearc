from .generator import generate_332efdb3
from .verifier import verify_332efdb3


TASK_ID = "332efdb3"
MAX_EXAMPLES = 900
generate = generate_332efdb3
verify = verify_332efdb3
REFERENCE_TASK_PATH = "data/official/arc2/training/332efdb3.json"

__all__ = [
    "TASK_ID",
    "MAX_EXAMPLES",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_332efdb3",
    "verify",
    "verify_332efdb3",
]
