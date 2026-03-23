from .generator import generate_20981f0e
from .verifier import verify_20981f0e


TASK_ID = "20981f0e"
generate = generate_20981f0e
verify = verify_20981f0e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/20981f0e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_20981f0e",
    "verify",
    "verify_20981f0e",
]
