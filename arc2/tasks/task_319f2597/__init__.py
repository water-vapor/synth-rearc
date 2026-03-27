from .generator import generate_319f2597
from .verifier import verify_319f2597


TASK_ID = "319f2597"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/319f2597.json"

generate = generate_319f2597
verify = verify_319f2597

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_319f2597",
    "verify",
    "verify_319f2597",
]
