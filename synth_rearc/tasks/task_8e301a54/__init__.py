from .generator import generate_8e301a54
from .verifier import verify_8e301a54


TASK_ID = "8e301a54"
generate = generate_8e301a54
verify = verify_8e301a54
REFERENCE_TASK_PATH = "data/official/arc2/training/8e301a54.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8e301a54",
    "verify",
    "verify_8e301a54",
]
