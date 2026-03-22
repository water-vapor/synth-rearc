from .generator import generate_7d18a6fb
from .verifier import verify_7d18a6fb


TASK_ID = "7d18a6fb"
generate = generate_7d18a6fb
verify = verify_7d18a6fb
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7d18a6fb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7d18a6fb",
    "verify",
    "verify_7d18a6fb",
]
