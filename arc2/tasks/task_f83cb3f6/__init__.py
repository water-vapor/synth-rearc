from .generator import generate_f83cb3f6
from .verifier import verify_f83cb3f6


TASK_ID = "f83cb3f6"
generate = generate_f83cb3f6
verify = verify_f83cb3f6
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f83cb3f6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f83cb3f6",
    "verify",
    "verify_f83cb3f6",
]
