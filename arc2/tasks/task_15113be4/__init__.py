from .generator import generate_15113be4
from .verifier import verify_15113be4


TASK_ID = "15113be4"
generate = generate_15113be4
verify = verify_15113be4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/15113be4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_15113be4",
    "verify",
    "verify_15113be4",
]
