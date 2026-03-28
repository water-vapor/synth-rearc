from .generator import generate_e7dd8335
from .verifier import verify_e7dd8335


TASK_ID = "e7dd8335"
generate = generate_e7dd8335
verify = verify_e7dd8335
REFERENCE_TASK_PATH = "data/official/arc2/training/e7dd8335.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e7dd8335",
    "verify",
    "verify_e7dd8335",
]
