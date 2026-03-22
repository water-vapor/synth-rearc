from .generator import generate_6ca952ad
from .verifier import verify_6ca952ad


TASK_ID = "6ca952ad"
generate = generate_6ca952ad
verify = verify_6ca952ad
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/6ca952ad.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6ca952ad",
    "verify",
    "verify_6ca952ad",
]
