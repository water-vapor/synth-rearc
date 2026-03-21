from .generator import generate_c92b942c
from .verifier import verify_c92b942c


TASK_ID = "c92b942c"
generate = generate_c92b942c
verify = verify_c92b942c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/c92b942c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c92b942c",
    "verify",
    "verify_c92b942c",
]
