from .generator import generate_8597cfd7
from .verifier import verify_8597cfd7


TASK_ID = "8597cfd7"
generate = generate_8597cfd7
verify = verify_8597cfd7
REFERENCE_TASK_PATH = "data/official/arc2/training/8597cfd7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8597cfd7",
    "verify",
    "verify_8597cfd7",
]
