from .generator import generate_458e3a53
from .verifier import verify_458e3a53


TASK_ID = "458e3a53"
generate = generate_458e3a53
verify = verify_458e3a53
REFERENCE_TASK_PATH = "data/official/arc2/training/458e3a53.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_458e3a53",
    "verify",
    "verify_458e3a53",
]
