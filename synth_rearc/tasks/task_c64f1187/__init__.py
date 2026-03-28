from .generator import generate_c64f1187
from .verifier import verify_c64f1187


TASK_ID = "c64f1187"
generate = generate_c64f1187
verify = verify_c64f1187
REFERENCE_TASK_PATH = "data/official/arc2/training/c64f1187.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c64f1187",
    "verify",
    "verify_c64f1187",
]
