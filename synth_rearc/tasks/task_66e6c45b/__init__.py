from .generator import generate_66e6c45b
from .verifier import verify_66e6c45b


TASK_ID = "66e6c45b"
MAX_EXAMPLES = 3024
REFERENCE_TASK_PATH = "data/official/arc2/training/66e6c45b.json"

generate = generate_66e6c45b
verify = verify_66e6c45b

__all__ = [
    "TASK_ID",
    "MAX_EXAMPLES",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_66e6c45b",
    "verify",
    "verify_66e6c45b",
]
