from .generator import generate_f823c43c
from .verifier import verify_f823c43c


TASK_ID = "f823c43c"
generate = generate_f823c43c
verify = verify_f823c43c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f823c43c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f823c43c",
    "verify",
    "verify_f823c43c",
]
