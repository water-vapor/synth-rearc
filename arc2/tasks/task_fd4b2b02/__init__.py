from .generator import generate_fd4b2b02
from .verifier import verify_fd4b2b02


TASK_ID = "fd4b2b02"
generate = generate_fd4b2b02
verify = verify_fd4b2b02
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fd4b2b02.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fd4b2b02",
    "verify",
    "verify_fd4b2b02",
]
