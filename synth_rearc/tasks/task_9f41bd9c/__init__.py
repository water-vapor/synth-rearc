from .generator import generate_9f41bd9c
from .verifier import verify_9f41bd9c


TASK_ID = "9f41bd9c"
generate = generate_9f41bd9c
verify = verify_9f41bd9c
REFERENCE_TASK_PATH = "data/official/arc2/training/9f41bd9c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9f41bd9c",
    "verify",
    "verify_9f41bd9c",
]
