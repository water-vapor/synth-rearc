from .generator import generate_c1990cce
from .verifier import verify_c1990cce


TASK_ID = "c1990cce"
generate = generate_c1990cce
verify = verify_c1990cce
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/c1990cce.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c1990cce",
    "verify",
    "verify_c1990cce",
]
