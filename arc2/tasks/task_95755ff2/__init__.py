from .generator import generate_95755ff2
from .verifier import verify_95755ff2


TASK_ID = "95755ff2"
generate = generate_95755ff2
verify = verify_95755ff2
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/95755ff2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_95755ff2",
    "verify",
    "verify_95755ff2",
]
