from .generator import generate_dd6b8c4b
from .verifier import verify_dd6b8c4b


TASK_ID = "dd6b8c4b"
generate = generate_dd6b8c4b
verify = verify_dd6b8c4b
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/dd6b8c4b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dd6b8c4b",
    "verify",
    "verify_dd6b8c4b",
]
