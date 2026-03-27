from .generator import generate_3391f8c0
from .verifier import verify_3391f8c0


TASK_ID = "3391f8c0"
generate = generate_3391f8c0
verify = verify_3391f8c0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/3391f8c0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3391f8c0",
    "verify",
    "verify_3391f8c0",
]
