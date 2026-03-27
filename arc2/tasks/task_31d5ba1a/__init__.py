from .generator import generate_31d5ba1a
from .verifier import verify_31d5ba1a


TASK_ID = "31d5ba1a"
generate = generate_31d5ba1a
verify = verify_31d5ba1a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/31d5ba1a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_31d5ba1a",
    "verify",
    "verify_31d5ba1a",
]
