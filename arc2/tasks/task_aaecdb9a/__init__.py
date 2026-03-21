from .generator import generate_aaecdb9a
from .verifier import verify_aaecdb9a


TASK_ID = "aaecdb9a"
generate = generate_aaecdb9a
verify = verify_aaecdb9a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/aaecdb9a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_aaecdb9a",
    "verify",
    "verify_aaecdb9a",
]
