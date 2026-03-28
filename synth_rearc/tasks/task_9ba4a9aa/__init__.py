from .generator import generate_9ba4a9aa
from .verifier import verify_9ba4a9aa


TASK_ID = "9ba4a9aa"
generate = generate_9ba4a9aa
verify = verify_9ba4a9aa
REFERENCE_TASK_PATH = "data/official/arc2/training/9ba4a9aa.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9ba4a9aa",
    "verify",
    "verify_9ba4a9aa",
]
