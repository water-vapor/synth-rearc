from .generator import generate_ed74f2f2
from .verifier import verify_ed74f2f2


TASK_ID = "ed74f2f2"
generate = generate_ed74f2f2
verify = verify_ed74f2f2
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ed74f2f2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ed74f2f2",
    "verify",
    "verify_ed74f2f2",
]
