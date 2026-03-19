from .generator import generate_e3fe1151
from .verifier import verify_e3fe1151


TASK_ID = "e3fe1151"
generate = generate_e3fe1151
verify = verify_e3fe1151
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e3fe1151.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e3fe1151",
    "verify",
    "verify_e3fe1151",
]
