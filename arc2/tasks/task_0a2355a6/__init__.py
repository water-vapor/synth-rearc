from .generator import generate_0a2355a6
from .verifier import verify_0a2355a6


TASK_ID = "0a2355a6"
generate = generate_0a2355a6
verify = verify_0a2355a6
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/0a2355a6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0a2355a6",
    "verify",
    "verify_0a2355a6",
]
