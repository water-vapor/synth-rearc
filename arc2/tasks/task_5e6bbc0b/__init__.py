from .generator import generate_5e6bbc0b
from .verifier import verify_5e6bbc0b


TASK_ID = "5e6bbc0b"
generate = generate_5e6bbc0b
verify = verify_5e6bbc0b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5e6bbc0b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5e6bbc0b",
    "verify",
    "verify_5e6bbc0b",
]
