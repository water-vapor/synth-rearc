from .generator import generate_1b8318e3
from .verifier import verify_1b8318e3


TASK_ID = "1b8318e3"
generate = generate_1b8318e3
verify = verify_1b8318e3
REFERENCE_TASK_PATH = "data/official/arc2/training/1b8318e3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1b8318e3",
    "verify",
    "verify_1b8318e3",
]
