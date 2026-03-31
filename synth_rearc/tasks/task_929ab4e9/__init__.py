from .generator import generate_929ab4e9
from .verifier import verify_929ab4e9


TASK_ID = "929ab4e9"
generate = generate_929ab4e9
verify = verify_929ab4e9
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/929ab4e9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_929ab4e9",
    "verify",
    "verify_929ab4e9",
]
