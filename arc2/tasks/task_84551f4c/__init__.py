from .generator import generate_84551f4c
from .verifier import verify_84551f4c


TASK_ID = "84551f4c"
generate = generate_84551f4c
verify = verify_84551f4c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/84551f4c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_84551f4c",
    "verify",
    "verify_84551f4c",
]
