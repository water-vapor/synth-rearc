from .generator import generate_e4888269
from .verifier import verify_e4888269


TASK_ID = "e4888269"
generate = generate_e4888269
verify = verify_e4888269
REFERENCE_TASK_PATH = "data/official/arc2/training/e4888269.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e4888269",
    "verify",
    "verify_e4888269",
]
