from .generator import generate_b15fca0b
from .verifier import verify_b15fca0b


TASK_ID = "b15fca0b"
generate = generate_b15fca0b
verify = verify_b15fca0b
REFERENCE_TASK_PATH = "data/official/arc2/training/b15fca0b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b15fca0b",
    "verify",
    "verify_b15fca0b",
]
