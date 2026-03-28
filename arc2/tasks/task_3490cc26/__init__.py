from .generator import generate_3490cc26
from .verifier import verify_3490cc26


TASK_ID = "3490cc26"
generate = generate_3490cc26
verify = verify_3490cc26
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/3490cc26.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3490cc26",
    "verify",
    "verify_3490cc26",
]
