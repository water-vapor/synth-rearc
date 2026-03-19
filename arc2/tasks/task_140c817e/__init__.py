from .generator import generate_140c817e
from .verifier import verify_140c817e


TASK_ID = "140c817e"
generate = generate_140c817e
verify = verify_140c817e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/140c817e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_140c817e",
    "verify",
    "verify_140c817e",
]
