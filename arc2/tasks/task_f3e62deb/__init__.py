from .generator import generate_f3e62deb
from .verifier import verify_f3e62deb


TASK_ID = "f3e62deb"
generate = generate_f3e62deb
verify = verify_f3e62deb
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f3e62deb.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f3e62deb",
    "verify",
    "verify_f3e62deb",
]
