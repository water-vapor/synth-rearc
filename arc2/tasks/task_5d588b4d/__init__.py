from .generator import generate_5d588b4d
from .verifier import verify_5d588b4d


TASK_ID = "5d588b4d"
generate = generate_5d588b4d
verify = verify_5d588b4d
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5d588b4d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5d588b4d",
    "verify",
    "verify_5d588b4d",
]
