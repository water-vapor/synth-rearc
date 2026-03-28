from .generator import generate_60d73be6
from .verifier import verify_60d73be6


TASK_ID = "60d73be6"
generate = generate_60d73be6
verify = verify_60d73be6
REFERENCE_TASK_PATH = "data/official/arc2/training/60d73be6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_60d73be6",
    "verify",
    "verify_60d73be6",
]
