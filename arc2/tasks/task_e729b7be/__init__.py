from .generator import generate_e729b7be
from .verifier import verify_e729b7be


TASK_ID = "e729b7be"
generate = generate_e729b7be
verify = verify_e729b7be
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e729b7be.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e729b7be",
    "verify",
    "verify_e729b7be",
]
