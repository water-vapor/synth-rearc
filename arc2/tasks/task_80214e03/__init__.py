from .generator import generate_80214e03
from .verifier import verify_80214e03


TASK_ID = "80214e03"
generate = generate_80214e03
verify = verify_80214e03
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/80214e03.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_80214e03",
    "verify",
    "verify_80214e03",
]
