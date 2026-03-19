from .generator import generate_e5790162
from .verifier import verify_e5790162


TASK_ID = "e5790162"
generate = generate_e5790162
verify = verify_e5790162
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e5790162.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e5790162",
    "verify",
    "verify_e5790162",
]
