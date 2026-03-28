from .generator import generate_4ff4c9da
from .verifier import verify_4ff4c9da


TASK_ID = "4ff4c9da"
generate = generate_4ff4c9da
verify = verify_4ff4c9da
REFERENCE_TASK_PATH = "data/official/arc2/training/4ff4c9da.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4ff4c9da",
    "verify",
    "verify_4ff4c9da",
]
