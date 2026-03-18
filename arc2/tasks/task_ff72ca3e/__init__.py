from .generator import generate_ff72ca3e
from .verifier import verify_ff72ca3e


TASK_ID = "ff72ca3e"
generate = generate_ff72ca3e
verify = verify_ff72ca3e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ff72ca3e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ff72ca3e",
    "verify",
    "verify_ff72ca3e",
]
