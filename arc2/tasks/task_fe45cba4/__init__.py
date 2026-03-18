from .generator import generate_fe45cba4
from .verifier import verify_fe45cba4


TASK_ID = "fe45cba4"
generate = generate_fe45cba4
verify = verify_fe45cba4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fe45cba4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fe45cba4",
    "verify",
    "verify_fe45cba4",
]
