from .generator import generate_4a1cacc2
from .verifier import verify_4a1cacc2


TASK_ID = "4a1cacc2"
generate = generate_4a1cacc2
verify = verify_4a1cacc2
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4a1cacc2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4a1cacc2",
    "verify",
    "verify_4a1cacc2",
]
