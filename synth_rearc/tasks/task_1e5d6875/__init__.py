from .generator import generate_1e5d6875
from .verifier import verify_1e5d6875


TASK_ID = "1e5d6875"
generate = generate_1e5d6875
verify = verify_1e5d6875
REFERENCE_TASK_PATH = "data/official/arc2/training/1e5d6875.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1e5d6875",
    "verify",
    "verify_1e5d6875",
]
