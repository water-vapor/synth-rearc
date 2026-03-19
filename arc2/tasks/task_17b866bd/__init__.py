from .generator import generate_17b866bd
from .verifier import verify_17b866bd


TASK_ID = "17b866bd"
generate = generate_17b866bd
verify = verify_17b866bd
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/17b866bd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_17b866bd",
    "verify",
    "verify_17b866bd",
]
