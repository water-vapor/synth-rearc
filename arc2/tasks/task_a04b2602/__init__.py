from .generator import generate_a04b2602
from .verifier import verify_a04b2602


TASK_ID = "a04b2602"
generate = generate_a04b2602
verify = verify_a04b2602
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a04b2602.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a04b2602",
    "verify",
    "verify_a04b2602",
]
