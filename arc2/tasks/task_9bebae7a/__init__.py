from .generator import generate_9bebae7a
from .verifier import verify_9bebae7a


TASK_ID = "9bebae7a"
generate = generate_9bebae7a
verify = verify_9bebae7a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9bebae7a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9bebae7a",
    "verify",
    "verify_9bebae7a",
]
