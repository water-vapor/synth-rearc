from .generator import generate_2c0b0aff
from .verifier import verify_2c0b0aff


TASK_ID = "2c0b0aff"
generate = generate_2c0b0aff
verify = verify_2c0b0aff
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/2c0b0aff.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2c0b0aff",
    "verify",
    "verify_2c0b0aff",
]
