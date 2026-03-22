from .generator import generate_891232d6
from .verifier import verify_891232d6


TASK_ID = "891232d6"
generate = generate_891232d6
verify = verify_891232d6
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/891232d6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_891232d6",
    "verify",
    "verify_891232d6",
]
