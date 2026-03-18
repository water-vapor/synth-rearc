from .generator import generate_f8cc533f
from .verifier import verify_f8cc533f


TASK_ID = "f8cc533f"
generate = generate_f8cc533f
verify = verify_f8cc533f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f8cc533f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f8cc533f",
    "verify",
    "verify_f8cc533f",
]
