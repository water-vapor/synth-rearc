from .generator import generate_fd096ab6
from .verifier import verify_fd096ab6


TASK_ID = "fd096ab6"
generate = generate_fd096ab6
verify = verify_fd096ab6
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fd096ab6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fd096ab6",
    "verify",
    "verify_fd096ab6",
]
