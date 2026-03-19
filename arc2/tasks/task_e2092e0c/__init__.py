from .generator import generate_e2092e0c
from .verifier import verify_e2092e0c


TASK_ID = "e2092e0c"
generate = generate_e2092e0c
verify = verify_e2092e0c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e2092e0c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e2092e0c",
    "verify",
    "verify_e2092e0c",
]
