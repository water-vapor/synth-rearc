from .generator import generate_97a05b5b
from .verifier import verify_97a05b5b


TASK_ID = "97a05b5b"
generate = generate_97a05b5b
verify = verify_97a05b5b
REFERENCE_TASK_PATH = "data/official/arc1/training/97a05b5b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_97a05b5b",
    "verify",
    "verify_97a05b5b",
]
