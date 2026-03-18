from .generator import generate_f0df5ff0
from .verifier import verify_f0df5ff0


TASK_ID = "f0df5ff0"
generate = generate_f0df5ff0
verify = verify_f0df5ff0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f0df5ff0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f0df5ff0",
    "verify",
    "verify_f0df5ff0",
]
