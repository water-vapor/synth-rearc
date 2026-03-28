from .generator import generate_42f14c03
from .verifier import verify_42f14c03


TASK_ID = "42f14c03"
generate = generate_42f14c03
verify = verify_42f14c03
REFERENCE_TASK_PATH = "data/official/arc2/training/42f14c03.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_42f14c03",
    "verify",
    "verify_42f14c03",
]
