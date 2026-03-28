from .generator import generate_0f63c0b9
from .verifier import verify_0f63c0b9


TASK_ID = "0f63c0b9"
generate = generate_0f63c0b9
verify = verify_0f63c0b9
REFERENCE_TASK_PATH = "data/official/arc2/training/0f63c0b9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0f63c0b9",
    "verify",
    "verify_0f63c0b9",
]
