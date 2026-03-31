from .generator import generate_6e453dd6
from .verifier import verify_6e453dd6


TASK_ID = "6e453dd6"
generate = generate_6e453dd6
verify = verify_6e453dd6
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/6e453dd6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6e453dd6",
    "verify",
    "verify_6e453dd6",
]
