from .generator import generate_dce56571
from .verifier import verify_dce56571


TASK_ID = "dce56571"
generate = generate_dce56571
verify = verify_dce56571
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/dce56571.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dce56571",
    "verify",
    "verify_dce56571",
]
