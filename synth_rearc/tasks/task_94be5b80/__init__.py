from .generator import generate_94be5b80
from .verifier import verify_94be5b80


TASK_ID = "94be5b80"
generate = generate_94be5b80
verify = verify_94be5b80
REFERENCE_TASK_PATH = "data/official/arc2/training/94be5b80.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_94be5b80",
    "verify",
    "verify_94be5b80",
]
