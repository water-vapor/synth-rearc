from .generator import generate_758abdf0
from .verifier import verify_758abdf0


TASK_ID = "758abdf0"
generate = generate_758abdf0
verify = verify_758abdf0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/758abdf0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_758abdf0",
    "verify",
    "verify_758abdf0",
]
