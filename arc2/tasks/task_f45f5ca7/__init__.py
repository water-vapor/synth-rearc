from .generator import generate_f45f5ca7
from .verifier import verify_f45f5ca7


TASK_ID = "f45f5ca7"
generate = generate_f45f5ca7
verify = verify_f45f5ca7
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f45f5ca7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f45f5ca7",
    "verify",
    "verify_f45f5ca7",
]
