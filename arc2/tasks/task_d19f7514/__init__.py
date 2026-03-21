from .generator import generate_d19f7514
from .verifier import verify_d19f7514


TASK_ID = "d19f7514"
generate = generate_d19f7514
verify = verify_d19f7514
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d19f7514.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d19f7514",
    "verify",
    "verify_d19f7514",
]
