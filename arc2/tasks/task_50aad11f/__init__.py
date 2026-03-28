from .generator import generate_50aad11f
from .verifier import verify_50aad11f


TASK_ID = "50aad11f"
generate = generate_50aad11f
verify = verify_50aad11f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/50aad11f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_50aad11f",
    "verify",
    "verify_50aad11f",
]
