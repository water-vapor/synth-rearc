from .generator import generate_1c0d0a4b
from .verifier import verify_1c0d0a4b


TASK_ID = "1c0d0a4b"
generate = generate_1c0d0a4b
verify = verify_1c0d0a4b
REFERENCE_TASK_PATH = "data/official/arc2/training/1c0d0a4b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1c0d0a4b",
    "verify",
    "verify_1c0d0a4b",
]
