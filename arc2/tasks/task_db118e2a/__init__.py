from .generator import generate_db118e2a
from .verifier import verify_db118e2a


TASK_ID = "db118e2a"
generate = generate_db118e2a
verify = verify_db118e2a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/db118e2a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_db118e2a",
    "verify",
    "verify_db118e2a",
]
