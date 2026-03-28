from .generator import generate_007bbfb7
from .verifier import verify_007bbfb7


TASK_ID = "007bbfb7"
REFERENCE_TASK_PATH = "data/official/arc1/training/007bbfb7.json"

generate = generate_007bbfb7
verify = verify_007bbfb7

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_007bbfb7",
    "verify",
    "verify_007bbfb7",
]
