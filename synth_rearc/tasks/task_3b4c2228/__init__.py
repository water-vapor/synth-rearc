from .generator import generate_3b4c2228
from .verifier import verify_3b4c2228


TASK_ID = "3b4c2228"
generate = generate_3b4c2228
verify = verify_3b4c2228
REFERENCE_TASK_PATH = "data/official/arc2/training/3b4c2228.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3b4c2228",
    "verify",
    "verify_3b4c2228",
]
