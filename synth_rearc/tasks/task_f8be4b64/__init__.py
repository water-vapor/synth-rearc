from .generator import generate_f8be4b64
from .verifier import verify_f8be4b64


TASK_ID = "f8be4b64"
generate = generate_f8be4b64
verify = verify_f8be4b64
REFERENCE_TASK_PATH = "data/official/arc2/training/f8be4b64.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f8be4b64",
    "verify",
    "verify_f8be4b64",
]
