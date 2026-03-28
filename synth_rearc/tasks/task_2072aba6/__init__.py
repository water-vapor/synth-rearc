from .generator import generate_2072aba6
from .verifier import verify_2072aba6


TASK_ID = "2072aba6"
generate = generate_2072aba6
verify = verify_2072aba6
REFERENCE_TASK_PATH = "data/official/arc2/training/2072aba6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2072aba6",
    "verify",
    "verify_2072aba6",
]
