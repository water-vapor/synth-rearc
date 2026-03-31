from .generator import generate_b5ca7ac4
from .verifier import verify_b5ca7ac4


TASK_ID = "b5ca7ac4"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/b5ca7ac4.json"

generate = generate_b5ca7ac4
verify = verify_b5ca7ac4

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b5ca7ac4",
    "verify",
    "verify_b5ca7ac4",
]
