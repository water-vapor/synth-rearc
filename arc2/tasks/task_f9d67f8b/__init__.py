from .generator import generate_f9d67f8b
from .verifier import verify_f9d67f8b


TASK_ID = "f9d67f8b"
generate = generate_f9d67f8b
verify = verify_f9d67f8b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f9d67f8b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f9d67f8b",
    "verify",
    "verify_f9d67f8b",
]
