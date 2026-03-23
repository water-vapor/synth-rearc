from .generator import generate_230f2e48
from .verifier import verify_230f2e48


TASK_ID = "230f2e48"
generate = generate_230f2e48
verify = verify_230f2e48
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/230f2e48.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_230f2e48",
    "verify",
    "verify_230f2e48",
]
