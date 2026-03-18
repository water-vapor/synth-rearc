from .generator import generate_137f0df0
from .verifier import verify_137f0df0


TASK_ID = "137f0df0"
generate = generate_137f0df0
verify = verify_137f0df0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/137f0df0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_137f0df0",
    "verify",
    "verify_137f0df0",
]
