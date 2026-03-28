from .generator import generate_bd5af378
from .verifier import verify_bd5af378


TASK_ID = "bd5af378"
generate = generate_bd5af378
verify = verify_bd5af378
REFERENCE_TASK_PATH = "data/official/arc2/training/bd5af378.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bd5af378",
    "verify",
    "verify_bd5af378",
]
