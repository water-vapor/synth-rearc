from .generator import generate_33b52de3
from .verifier import verify_33b52de3


TASK_ID = "33b52de3"
generate = generate_33b52de3
verify = verify_33b52de3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/33b52de3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_33b52de3",
    "verify",
    "verify_33b52de3",
]
