from .generator import generate_d931c21c
from .verifier import verify_d931c21c


TASK_ID = "d931c21c"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d931c21c.json"

generate = generate_d931c21c
verify = verify_d931c21c


__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "verify",
    "generate_d931c21c",
    "verify_d931c21c",
]
