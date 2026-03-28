from .generator import generate_342dd610
from .verifier import verify_342dd610


TASK_ID = "342dd610"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/342dd610.json"

generate = generate_342dd610
verify = verify_342dd610

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_342dd610",
    "verify",
    "verify_342dd610",
]
