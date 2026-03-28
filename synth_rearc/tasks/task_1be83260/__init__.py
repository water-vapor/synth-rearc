from .generator import generate_1be83260
from .verifier import verify_1be83260


TASK_ID = "1be83260"
generate = generate_1be83260
verify = verify_1be83260
REFERENCE_TASK_PATH = "data/official/arc2/training/1be83260.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1be83260",
    "verify",
    "verify_1be83260",
]
