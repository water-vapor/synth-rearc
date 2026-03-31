from .generator import generate_58f5dbd5
from .verifier import verify_58f5dbd5


TASK_ID = "58f5dbd5"
generate = generate_58f5dbd5
verify = verify_58f5dbd5
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/58f5dbd5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_58f5dbd5",
    "verify",
    "verify_58f5dbd5",
]
