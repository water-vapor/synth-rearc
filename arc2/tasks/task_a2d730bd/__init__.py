from .generator import generate_a2d730bd
from .verifier import verify_a2d730bd


TASK_ID = "a2d730bd"
generate = generate_a2d730bd
verify = verify_a2d730bd
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a2d730bd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a2d730bd",
    "verify",
    "verify_a2d730bd",
]
