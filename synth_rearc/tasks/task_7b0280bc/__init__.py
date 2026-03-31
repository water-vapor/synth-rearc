from .generator import generate_7b0280bc
from .verifier import verify_7b0280bc


TASK_ID = "7b0280bc"
generate = generate_7b0280bc
verify = verify_7b0280bc
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/7b0280bc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7b0280bc",
    "verify",
    "verify_7b0280bc",
]
