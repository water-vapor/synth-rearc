from .generator import generate_f931b4a8
from .verifier import verify_f931b4a8


TASK_ID = "f931b4a8"
generate = generate_f931b4a8
verify = verify_f931b4a8
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/f931b4a8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f931b4a8",
    "verify",
    "verify_f931b4a8",
]
