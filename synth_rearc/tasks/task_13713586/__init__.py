from .generator import generate_13713586
from .verifier import verify_13713586


TASK_ID = "13713586"
generate = generate_13713586
verify = verify_13713586
REFERENCE_TASK_PATH = "data/official/arc2/training/13713586.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_13713586",
    "verify",
    "verify_13713586",
]
