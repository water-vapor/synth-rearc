from .generator import generate_f341894c
from .verifier import verify_f341894c


TASK_ID = "f341894c"
generate = generate_f341894c
verify = verify_f341894c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f341894c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f341894c",
    "verify",
    "verify_f341894c",
]
