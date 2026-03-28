from .generator import generate_73c3b0d8
from .verifier import verify_73c3b0d8


TASK_ID = "73c3b0d8"
generate = generate_73c3b0d8
verify = verify_73c3b0d8
REFERENCE_TASK_PATH = "data/official/arc2/training/73c3b0d8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_73c3b0d8",
    "verify",
    "verify_73c3b0d8",
]
