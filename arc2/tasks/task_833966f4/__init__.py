from .generator import generate_833966f4
from .verifier import verify_833966f4


TASK_ID = "833966f4"
generate = generate_833966f4
verify = verify_833966f4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/833966f4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_833966f4",
    "verify",
    "verify_833966f4",
]
