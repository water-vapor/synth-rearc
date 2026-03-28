from .generator import generate_4e45f183
from .verifier import verify_4e45f183


TASK_ID = "4e45f183"
generate = generate_4e45f183
verify = verify_4e45f183
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4e45f183.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4e45f183",
    "verify",
    "verify_4e45f183",
]
