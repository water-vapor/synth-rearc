from .generator import generate_00dbd492
from .verifier import verify_00dbd492


TASK_ID = "00dbd492"
generate = generate_00dbd492
verify = verify_00dbd492
REFERENCE_TASK_PATH = "data/official/arc2/training/00dbd492.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_00dbd492",
    "verify",
    "verify_00dbd492",
]
