from .generator import generate_fd02da9e
from .verifier import verify_fd02da9e


TASK_ID = "fd02da9e"
generate = generate_fd02da9e
verify = verify_fd02da9e
REFERENCE_TASK_PATH = "data/official/arc2/training/fd02da9e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fd02da9e",
    "verify",
    "verify_fd02da9e",
]
