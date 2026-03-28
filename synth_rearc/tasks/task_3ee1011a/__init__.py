from .generator import generate_3ee1011a
from .verifier import verify_3ee1011a


TASK_ID = "3ee1011a"
generate = generate_3ee1011a
verify = verify_3ee1011a
REFERENCE_TASK_PATH = "data/official/arc2/training/3ee1011a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3ee1011a",
    "verify",
    "verify_3ee1011a",
]
