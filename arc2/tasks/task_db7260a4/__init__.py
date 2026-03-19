from .generator import generate_db7260a4
from .verifier import verify_db7260a4


TASK_ID = "db7260a4"
generate = generate_db7260a4
verify = verify_db7260a4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/db7260a4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_db7260a4",
    "verify",
    "verify_db7260a4",
]
