from .generator import generate_dc2aa30b
from .verifier import verify_dc2aa30b


TASK_ID = "dc2aa30b"
generate = generate_dc2aa30b
verify = verify_dc2aa30b
REFERENCE_TASK_PATH = "data/official/arc2/training/dc2aa30b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dc2aa30b",
    "verify",
    "verify_dc2aa30b",
]
