from .generator import generate_470c91de
from .verifier import verify_470c91de


TASK_ID = "470c91de"
generate = generate_470c91de
verify = verify_470c91de
REFERENCE_TASK_PATH = "data/official/arc2/training/470c91de.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_470c91de",
    "verify",
    "verify_470c91de",
]
