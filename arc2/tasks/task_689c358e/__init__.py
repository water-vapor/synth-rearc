from .generator import generate_689c358e
from .verifier import verify_689c358e


TASK_ID = "689c358e"
generate = generate_689c358e
verify = verify_689c358e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/689c358e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_689c358e",
    "verify",
    "verify_689c358e",
]
