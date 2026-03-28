from .generator import generate_e88171ec
from .verifier import verify_e88171ec


TASK_ID = "e88171ec"
generate = generate_e88171ec
verify = verify_e88171ec
REFERENCE_TASK_PATH = "data/official/arc2/training/e88171ec.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e88171ec",
    "verify",
    "verify_e88171ec",
]
