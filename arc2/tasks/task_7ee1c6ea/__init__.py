from .generator import generate_7ee1c6ea
from .verifier import verify_7ee1c6ea


TASK_ID = "7ee1c6ea"
generate = generate_7ee1c6ea
verify = verify_7ee1c6ea
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7ee1c6ea.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7ee1c6ea",
    "verify",
    "verify_7ee1c6ea",
]
