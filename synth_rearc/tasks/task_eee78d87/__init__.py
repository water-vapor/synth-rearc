from .generator import generate_eee78d87
from .verifier import verify_eee78d87


TASK_ID = "eee78d87"
generate = generate_eee78d87
verify = verify_eee78d87
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/eee78d87.json"
MAX_EXAMPLES = 1152

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "MAX_EXAMPLES",
    "generate",
    "generate_eee78d87",
    "verify",
    "verify_eee78d87",
]
