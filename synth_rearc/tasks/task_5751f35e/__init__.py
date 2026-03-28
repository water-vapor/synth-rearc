from .generator import generate_5751f35e
from .verifier import verify_5751f35e


TASK_ID = "5751f35e"
generate = generate_5751f35e
verify = verify_5751f35e
REFERENCE_TASK_PATH = "data/official/arc2/training/5751f35e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5751f35e",
    "verify",
    "verify_5751f35e",
]
