from .generator import generate_825aa9e9
from .verifier import verify_825aa9e9


TASK_ID = "825aa9e9"
generate = generate_825aa9e9
verify = verify_825aa9e9
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/825aa9e9.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_825aa9e9",
    "verify",
    "verify_825aa9e9",
]
