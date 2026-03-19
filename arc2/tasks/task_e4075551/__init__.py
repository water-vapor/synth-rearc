from .generator import generate_e4075551
from .verifier import verify_e4075551


TASK_ID = "e4075551"
generate = generate_e4075551
verify = verify_e4075551
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e4075551.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e4075551",
    "verify",
    "verify_e4075551",
]
