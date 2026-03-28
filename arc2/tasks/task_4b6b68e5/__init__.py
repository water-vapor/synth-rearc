from .generator import generate_4b6b68e5
from .verifier import verify_4b6b68e5


TASK_ID = "4b6b68e5"
generate = generate_4b6b68e5
verify = verify_4b6b68e5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4b6b68e5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4b6b68e5",
    "verify",
    "verify_4b6b68e5",
]
