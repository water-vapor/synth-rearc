from .generator import generate_f9a67cb5
from .verifier import verify_f9a67cb5


TASK_ID = "f9a67cb5"
generate = generate_f9a67cb5
verify = verify_f9a67cb5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f9a67cb5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f9a67cb5",
    "verify",
    "verify_f9a67cb5",
]
