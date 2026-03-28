from .generator import generate_7c9b52a0
from .verifier import verify_7c9b52a0


TASK_ID = "7c9b52a0"
generate = generate_7c9b52a0
verify = verify_7c9b52a0
REFERENCE_TASK_PATH = "data/official/arc2/training/7c9b52a0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7c9b52a0",
    "verify",
    "verify_7c9b52a0",
]
