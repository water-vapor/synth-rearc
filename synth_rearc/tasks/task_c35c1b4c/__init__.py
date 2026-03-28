from .generator import generate_c35c1b4c
from .verifier import verify_c35c1b4c


TASK_ID = "c35c1b4c"
generate = generate_c35c1b4c
verify = verify_c35c1b4c
REFERENCE_TASK_PATH = "data/official/arc2/training/c35c1b4c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c35c1b4c",
    "verify",
    "verify_c35c1b4c",
]
