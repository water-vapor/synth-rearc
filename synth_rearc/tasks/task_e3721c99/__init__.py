from .generator import generate_e3721c99
from .verifier import verify_e3721c99


TASK_ID = "e3721c99"
generate = generate_e3721c99
verify = verify_e3721c99
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/e3721c99.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e3721c99",
    "verify",
    "verify_e3721c99",
]
