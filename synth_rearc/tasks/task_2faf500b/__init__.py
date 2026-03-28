from .generator import generate_2faf500b
from .verifier import verify_2faf500b


TASK_ID = "2faf500b"
generate = generate_2faf500b
verify = verify_2faf500b
REFERENCE_TASK_PATH = "data/official/arc2/training/2faf500b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2faf500b",
    "verify",
    "verify_2faf500b",
]
