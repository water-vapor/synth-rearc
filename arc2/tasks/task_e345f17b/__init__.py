from .generator import generate_e345f17b
from .verifier import verify_e345f17b


TASK_ID = "e345f17b"
generate = generate_e345f17b
verify = verify_e345f17b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e345f17b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e345f17b",
    "verify",
    "verify_e345f17b",
]
