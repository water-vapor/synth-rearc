from .generator import generate_d56f2372
from .verifier import verify_d56f2372


TASK_ID = "d56f2372"
generate = generate_d56f2372
verify = verify_d56f2372
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d56f2372.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d56f2372",
    "verify",
    "verify_d56f2372",
]
