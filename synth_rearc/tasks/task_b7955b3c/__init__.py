from .generator import generate_b7955b3c
from .verifier import verify_b7955b3c


TASK_ID = "b7955b3c"
generate = generate_b7955b3c
verify = verify_b7955b3c
REFERENCE_TASK_PATH = "data/official/arc2/training/b7955b3c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b7955b3c",
    "verify",
    "verify_b7955b3c",
]
