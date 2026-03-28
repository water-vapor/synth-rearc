from .generator import generate_465b7d93
from .verifier import verify_465b7d93


TASK_ID = "465b7d93"
generate = generate_465b7d93
verify = verify_465b7d93
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/465b7d93.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_465b7d93",
    "verify",
    "verify_465b7d93",
]
