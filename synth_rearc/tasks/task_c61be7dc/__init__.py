from .generator import generate_c61be7dc
from .verifier import verify_c61be7dc


TASK_ID = "c61be7dc"
generate = generate_c61be7dc
verify = verify_c61be7dc
REFERENCE_TASK_PATH = "data/official/arc2/training/c61be7dc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c61be7dc",
    "verify",
    "verify_c61be7dc",
]
