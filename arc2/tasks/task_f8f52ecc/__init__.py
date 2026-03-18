from .generator import generate_f8f52ecc
from .verifier import verify_f8f52ecc


TASK_ID = "f8f52ecc"
generate = generate_f8f52ecc
verify = verify_f8f52ecc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f8f52ecc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f8f52ecc",
    "verify",
    "verify_f8f52ecc",
]
