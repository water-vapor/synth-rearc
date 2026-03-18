from .generator import generate_11e1fe23
from .verifier import verify_11e1fe23


TASK_ID = "11e1fe23"
generate = generate_11e1fe23
verify = verify_11e1fe23
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/11e1fe23.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_11e1fe23",
    "verify",
    "verify_11e1fe23",
]
