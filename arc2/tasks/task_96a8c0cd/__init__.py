from .generator import generate_96a8c0cd
from .verifier import verify_96a8c0cd


TASK_ID = "96a8c0cd"
generate = generate_96a8c0cd
verify = verify_96a8c0cd
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/96a8c0cd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_96a8c0cd",
    "verify",
    "verify_96a8c0cd",
]
