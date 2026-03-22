from .generator import generate_6ea4a07e
from .verifier import verify_6ea4a07e


TASK_ID = "6ea4a07e"
MAX_EXAMPLES = 1116
generate = generate_6ea4a07e
verify = verify_6ea4a07e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/6ea4a07e.json"

__all__ = [
    "TASK_ID",
    "MAX_EXAMPLES",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_6ea4a07e",
    "verify",
    "verify_6ea4a07e",
]
