from .generator import generate_03560426
from .verifier import verify_03560426


TASK_ID = "03560426"
generate = generate_03560426
verify = verify_03560426
REFERENCE_TASK_PATH = "data/official/arc2/training/03560426.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_03560426",
    "verify",
    "verify_03560426",
]
