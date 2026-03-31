from .generator import generate_1818057f
from .verifier import verify_1818057f


TASK_ID = "1818057f"
generate = generate_1818057f
verify = verify_1818057f
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/1818057f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1818057f",
    "verify",
    "verify_1818057f",
]
