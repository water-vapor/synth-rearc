from .generator import generate_d4c90558
from .verifier import verify_d4c90558


TASK_ID = "d4c90558"
generate = generate_d4c90558
verify = verify_d4c90558
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d4c90558.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d4c90558",
    "verify",
    "verify_d4c90558",
]
