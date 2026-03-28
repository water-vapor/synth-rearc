from .generator import generate_642248e4
from .verifier import verify_642248e4


TASK_ID = "642248e4"
generate = generate_642248e4
verify = verify_642248e4
REFERENCE_TASK_PATH = "data/official/arc2/training/642248e4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_642248e4",
    "verify",
    "verify_642248e4",
]
