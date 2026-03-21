from .generator import generate_9b30e358
from .verifier import verify_9b30e358


TASK_ID = "9b30e358"
generate = generate_9b30e358
verify = verify_9b30e358
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9b30e358.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9b30e358",
    "verify",
    "verify_9b30e358",
]
