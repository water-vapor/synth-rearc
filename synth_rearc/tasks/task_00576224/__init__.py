from .generator import generate_00576224
from .verifier import verify_00576224


TASK_ID = "00576224"
generate = generate_00576224
verify = verify_00576224
REFERENCE_TASK_PATH = "data/official/arc2/training/00576224.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_00576224",
    "verify",
    "verify_00576224",
]
