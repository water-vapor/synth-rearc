from .generator import generate_f18ec8cc
from .verifier import verify_f18ec8cc


TASK_ID = "f18ec8cc"
generate = generate_f18ec8cc
verify = verify_f18ec8cc
REFERENCE_TASK_PATH = "data/official/arc2/training/f18ec8cc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f18ec8cc",
    "verify",
    "verify_f18ec8cc",
]
