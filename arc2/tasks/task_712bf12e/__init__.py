from .generator import generate_712bf12e
from .verifier import verify_712bf12e


TASK_ID = "712bf12e"
generate = generate_712bf12e
verify = verify_712bf12e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/712bf12e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_712bf12e",
    "verify",
    "verify_712bf12e",
]
