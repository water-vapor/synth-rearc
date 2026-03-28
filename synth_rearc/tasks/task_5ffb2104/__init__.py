from .generator import generate_5ffb2104
from .verifier import verify_5ffb2104


TASK_ID = "5ffb2104"
generate = generate_5ffb2104
verify = verify_5ffb2104
REFERENCE_TASK_PATH = "data/official/arc2/training/5ffb2104.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5ffb2104",
    "verify",
    "verify_5ffb2104",
]
