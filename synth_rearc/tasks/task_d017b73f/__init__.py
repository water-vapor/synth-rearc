from .generator import generate_d017b73f
from .verifier import verify_d017b73f


TASK_ID = "d017b73f"
generate = generate_d017b73f
verify = verify_d017b73f
REFERENCE_TASK_PATH = "data/official/arc2/training/d017b73f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d017b73f",
    "verify",
    "verify_d017b73f",
]
