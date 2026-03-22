from .generator import generate_92e50de0
from .verifier import verify_92e50de0


TASK_ID = "92e50de0"
generate = generate_92e50de0
verify = verify_92e50de0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/92e50de0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_92e50de0",
    "verify",
    "verify_92e50de0",
]
