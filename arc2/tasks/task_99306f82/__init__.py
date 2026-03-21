from .generator import generate_99306f82
from .verifier import verify_99306f82


TASK_ID = "99306f82"
generate = generate_99306f82
verify = verify_99306f82
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/99306f82.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_99306f82",
    "verify",
    "verify_99306f82",
]
