from .generator import generate_7d7772cc
from .verifier import verify_7d7772cc


TASK_ID = "7d7772cc"
generate = generate_7d7772cc
verify = verify_7d7772cc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7d7772cc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7d7772cc",
    "verify",
    "verify_7d7772cc",
]
