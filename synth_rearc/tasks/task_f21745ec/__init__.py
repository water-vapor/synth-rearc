from .generator import generate_f21745ec
from .verifier import verify_f21745ec


TASK_ID = "f21745ec"
generate = generate_f21745ec
verify = verify_f21745ec
REFERENCE_TASK_PATH = "data/official/arc2/training/f21745ec.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f21745ec",
    "verify",
    "verify_f21745ec",
]
