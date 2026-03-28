from .generator import generate_5207a7b5
from .verifier import verify_5207a7b5


TASK_ID = "5207a7b5"
generate = generate_5207a7b5
verify = verify_5207a7b5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5207a7b5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5207a7b5",
    "verify",
    "verify_5207a7b5",
]
