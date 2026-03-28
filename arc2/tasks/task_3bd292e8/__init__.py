from .generator import generate_3bd292e8
from .verifier import verify_3bd292e8


TASK_ID = "3bd292e8"
generate = generate_3bd292e8
verify = verify_3bd292e8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/3bd292e8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3bd292e8",
    "verify",
    "verify_3bd292e8",
]
