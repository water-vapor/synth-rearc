from .generator import generate_e760a62e
from .verifier import verify_e760a62e


TASK_ID = "e760a62e"
generate = generate_e760a62e
verify = verify_e760a62e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e760a62e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e760a62e",
    "verify",
    "verify_e760a62e",
]
