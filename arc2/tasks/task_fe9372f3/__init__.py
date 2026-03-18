from .generator import generate_fe9372f3
from .verifier import verify_fe9372f3


TASK_ID = "fe9372f3"
generate = generate_fe9372f3
verify = verify_fe9372f3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fe9372f3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fe9372f3",
    "verify",
    "verify_fe9372f3",
]
