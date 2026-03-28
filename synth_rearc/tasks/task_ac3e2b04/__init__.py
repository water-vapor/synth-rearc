from .generator import generate_ac3e2b04
from .verifier import verify_ac3e2b04


TASK_ID = "ac3e2b04"
generate = generate_ac3e2b04
verify = verify_ac3e2b04
REFERENCE_TASK_PATH = "data/official/arc2/training/ac3e2b04.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ac3e2b04",
    "verify",
    "verify_ac3e2b04",
]
