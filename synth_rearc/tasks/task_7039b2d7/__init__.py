from .generator import generate_7039b2d7
from .verifier import verify_7039b2d7


TASK_ID = "7039b2d7"
generate = generate_7039b2d7
verify = verify_7039b2d7
REFERENCE_TASK_PATH = "data/official/arc2/training/7039b2d7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7039b2d7",
    "verify",
    "verify_7039b2d7",
]
