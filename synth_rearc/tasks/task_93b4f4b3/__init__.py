from .generator import generate_93b4f4b3
from .verifier import verify_93b4f4b3


TASK_ID = "93b4f4b3"
generate = generate_93b4f4b3
verify = verify_93b4f4b3
REFERENCE_TASK_PATH = "data/official/arc2/training/93b4f4b3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_93b4f4b3",
    "verify",
    "verify_93b4f4b3",
]
