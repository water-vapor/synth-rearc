from .generator import generate_bcb3040b
from .verifier import verify_bcb3040b


TASK_ID = "bcb3040b"
generate = generate_bcb3040b
verify = verify_bcb3040b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/bcb3040b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bcb3040b",
    "verify",
    "verify_bcb3040b",
]
