from .generator import generate_a6953f00
from .verifier import verify_a6953f00


TASK_ID = "a6953f00"
generate = generate_a6953f00
verify = verify_a6953f00
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a6953f00.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a6953f00",
    "verify",
    "verify_a6953f00",
]
