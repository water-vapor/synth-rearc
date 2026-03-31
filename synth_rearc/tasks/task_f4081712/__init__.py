from .generator import generate_f4081712
from .verifier import verify_f4081712


TASK_ID = "f4081712"
generate = generate_f4081712
verify = verify_f4081712
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/f4081712.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f4081712",
    "verify",
    "verify_f4081712",
]
