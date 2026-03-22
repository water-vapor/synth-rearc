from .generator import generate_7d419a02
from .verifier import verify_7d419a02


TASK_ID = "7d419a02"
generate = generate_7d419a02
verify = verify_7d419a02
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/7d419a02.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7d419a02",
    "verify",
    "verify_7d419a02",
]
