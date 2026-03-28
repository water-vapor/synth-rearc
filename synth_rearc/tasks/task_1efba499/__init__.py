from .generator import generate_1efba499
from .verifier import verify_1efba499


TASK_ID = "1efba499"
generate = generate_1efba499
verify = verify_1efba499
REFERENCE_TASK_PATH = "data/official/arc2/training/1efba499.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1efba499",
    "verify",
    "verify_1efba499",
]
