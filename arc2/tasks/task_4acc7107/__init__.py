from .generator import generate_4acc7107
from .verifier import verify_4acc7107


TASK_ID = "4acc7107"
generate = generate_4acc7107
verify = verify_4acc7107
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4acc7107.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4acc7107",
    "verify",
    "verify_4acc7107",
]
