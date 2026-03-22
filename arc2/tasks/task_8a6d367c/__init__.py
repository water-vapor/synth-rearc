from .generator import generate_8a6d367c
from .verifier import verify_8a6d367c


TASK_ID = "8a6d367c"
generate = generate_8a6d367c
verify = verify_8a6d367c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/8a6d367c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8a6d367c",
    "verify",
    "verify_8a6d367c",
]
