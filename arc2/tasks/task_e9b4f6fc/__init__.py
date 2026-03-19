from .generator import generate_e9b4f6fc
from .verifier import verify_e9b4f6fc


TASK_ID = "e9b4f6fc"
generate = generate_e9b4f6fc
verify = verify_e9b4f6fc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e9b4f6fc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e9b4f6fc",
    "verify",
    "verify_e9b4f6fc",
]
