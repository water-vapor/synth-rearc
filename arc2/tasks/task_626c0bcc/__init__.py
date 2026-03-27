from .generator import generate_626c0bcc
from .verifier import verify_626c0bcc


TASK_ID = "626c0bcc"
generate = generate_626c0bcc
verify = verify_626c0bcc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/626c0bcc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_626c0bcc",
    "verify",
    "verify_626c0bcc",
]
