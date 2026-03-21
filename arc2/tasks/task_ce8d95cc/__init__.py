from .generator import generate_ce8d95cc
from .verifier import verify_ce8d95cc


TASK_ID = "ce8d95cc"
generate = generate_ce8d95cc
verify = verify_ce8d95cc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ce8d95cc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ce8d95cc",
    "verify",
    "verify_ce8d95cc",
]
