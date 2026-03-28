from .generator import generate_0607ce86
from .verifier import verify_0607ce86


TASK_ID = "0607ce86"
generate = generate_0607ce86
verify = verify_0607ce86
REFERENCE_TASK_PATH = "data/official/arc2/training/0607ce86.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0607ce86",
    "verify",
    "verify_0607ce86",
]
