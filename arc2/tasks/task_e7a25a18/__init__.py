from .generator import generate_e7a25a18
from .verifier import verify_e7a25a18


TASK_ID = "e7a25a18"
generate = generate_e7a25a18
verify = verify_e7a25a18
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e7a25a18.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e7a25a18",
    "verify",
    "verify_e7a25a18",
]
