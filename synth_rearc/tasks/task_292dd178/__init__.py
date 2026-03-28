from .generator import generate_292dd178
from .verifier import verify_292dd178


TASK_ID = "292dd178"
generate = generate_292dd178
verify = verify_292dd178
REFERENCE_TASK_PATH = "data/official/arc2/training/292dd178.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_292dd178",
    "verify",
    "verify_292dd178",
]
