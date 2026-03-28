from .generator import generate_42918530
from .verifier import verify_42918530


TASK_ID = "42918530"
generate = generate_42918530
verify = verify_42918530
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/42918530.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_42918530",
    "verify",
    "verify_42918530",
]
