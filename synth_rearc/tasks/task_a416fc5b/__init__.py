from .generator import generate_a416fc5b
from .verifier import verify_a416fc5b


TASK_ID = "a416fc5b"
MAX_EXAMPLES = 16
generate = generate_a416fc5b
verify = verify_a416fc5b
REFERENCE_TASK_PATH = "data/official/arc2/training/a416fc5b.json"

__all__ = [
    "TASK_ID",
    "MAX_EXAMPLES",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a416fc5b",
    "verify",
    "verify_a416fc5b",
]
