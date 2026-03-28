from .generator import generate_8fbca751
from .verifier import verify_8fbca751


TASK_ID = "8fbca751"
generate = generate_8fbca751
verify = verify_8fbca751
REFERENCE_TASK_PATH = "data/official/arc2/training/8fbca751.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8fbca751",
    "verify",
    "verify_8fbca751",
]
