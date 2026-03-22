from .generator import generate_72a961c9
from .verifier import verify_72a961c9


TASK_ID = "72a961c9"
generate = generate_72a961c9
verify = verify_72a961c9
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/72a961c9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_72a961c9",
    "verify",
    "verify_72a961c9",
]
