from .generator import generate_12422b43
from .verifier import verify_12422b43


TASK_ID = "12422b43"
generate = generate_12422b43
verify = verify_12422b43
REFERENCE_TASK_PATH = "data/official/arc2/training/12422b43.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_12422b43",
    "verify",
    "verify_12422b43",
]
