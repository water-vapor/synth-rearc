from .generator import generate_7c8af763
from .verifier import verify_7c8af763


TASK_ID = "7c8af763"
generate = generate_7c8af763
verify = verify_7c8af763
REFERENCE_TASK_PATH = "data/official/arc2/training/7c8af763.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7c8af763",
    "verify",
    "verify_7c8af763",
]
