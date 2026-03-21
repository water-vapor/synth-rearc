from .generator import generate_ce039d91
from .verifier import verify_ce039d91


TASK_ID = "ce039d91"
generate = generate_ce039d91
verify = verify_ce039d91
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ce039d91.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ce039d91",
    "verify",
    "verify_ce039d91",
]
