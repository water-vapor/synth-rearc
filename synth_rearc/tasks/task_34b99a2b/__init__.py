from .generator import generate_34b99a2b
from .verifier import verify_34b99a2b


TASK_ID = "34b99a2b"
generate = generate_34b99a2b
verify = verify_34b99a2b
REFERENCE_TASK_PATH = "data/official/arc2/training/34b99a2b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_34b99a2b",
    "verify",
    "verify_34b99a2b",
]
