from .generator import generate_1190bc91
from .verifier import verify_1190bc91


TASK_ID = "1190bc91"
generate = generate_1190bc91
verify = verify_1190bc91
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1190bc91.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1190bc91",
    "verify",
    "verify_1190bc91",
]
