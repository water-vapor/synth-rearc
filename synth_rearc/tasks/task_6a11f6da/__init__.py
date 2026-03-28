from .generator import generate_6a11f6da
from .verifier import verify_6a11f6da


TASK_ID = "6a11f6da"
generate = generate_6a11f6da
verify = verify_6a11f6da
REFERENCE_TASK_PATH = "data/official/arc2/training/6a11f6da.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6a11f6da",
    "verify",
    "verify_6a11f6da",
]
