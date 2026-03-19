from .generator import generate_1990f7a8
from .verifier import verify_1990f7a8


TASK_ID = "1990f7a8"
generate = generate_1990f7a8
verify = verify_1990f7a8
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1990f7a8.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1990f7a8",
    "verify",
    "verify_1990f7a8",
]
