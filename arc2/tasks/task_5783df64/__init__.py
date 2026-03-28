from .generator import generate_5783df64
from .verifier import verify_5783df64


TASK_ID = "5783df64"
generate = generate_5783df64
verify = verify_5783df64
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5783df64.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5783df64",
    "verify",
    "verify_5783df64",
]
