from .generator import generate_55059096
from .verifier import verify_55059096


TASK_ID = "55059096"
generate = generate_55059096
verify = verify_55059096
REFERENCE_TASK_PATH = "data/official/arc2/training/55059096.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_55059096",
    "verify",
    "verify_55059096",
]
