from .generator import generate_48131b3c
from .verifier import verify_48131b3c


TASK_ID = "48131b3c"
generate = generate_48131b3c
verify = verify_48131b3c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/48131b3c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_48131b3c",
    "verify",
    "verify_48131b3c",
]
