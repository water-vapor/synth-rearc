from .generator import generate_22806e14
from .verifier import verify_22806e14


TASK_ID = "22806e14"
generate = generate_22806e14
verify = verify_22806e14
REFERENCE_TASK_PATH = "data/official/arc2/training/22806e14.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_22806e14",
    "verify",
    "verify_22806e14",
]
