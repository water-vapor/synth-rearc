from .generator import generate_84f2aca1
from .verifier import verify_84f2aca1


TASK_ID = "84f2aca1"
generate = generate_84f2aca1
verify = verify_84f2aca1
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/84f2aca1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_84f2aca1",
    "verify",
    "verify_84f2aca1",
]
