from .generator import generate_898e7135
from .verifier import verify_898e7135


TASK_ID = "898e7135"
generate = generate_898e7135
verify = verify_898e7135
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/898e7135.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_898e7135",
    "verify",
    "verify_898e7135",
]
