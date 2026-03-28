from .generator import generate_5b526a93
from .verifier import verify_5b526a93


TASK_ID = "5b526a93"
generate = generate_5b526a93
verify = verify_5b526a93
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5b526a93.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5b526a93",
    "verify",
    "verify_5b526a93",
]
