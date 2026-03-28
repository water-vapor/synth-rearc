from .generator import generate_fbf15a0b
from .verifier import verify_fbf15a0b


TASK_ID = "fbf15a0b"
generate = generate_fbf15a0b
verify = verify_fbf15a0b
REFERENCE_TASK_PATH = "data/official/arc2/training/fbf15a0b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fbf15a0b",
    "verify",
    "verify_fbf15a0b",
]
