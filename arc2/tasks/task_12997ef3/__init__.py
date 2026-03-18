from .generator import generate_12997ef3
from .verifier import verify_12997ef3


TASK_ID = "12997ef3"
generate = generate_12997ef3
verify = verify_12997ef3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/12997ef3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_12997ef3",
    "verify",
    "verify_12997ef3",
]
