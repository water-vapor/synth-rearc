from .generator import generate_f3e14006
from .verifier import verify_f3e14006


TASK_ID = "f3e14006"
generate = generate_f3e14006
verify = verify_f3e14006
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f3e14006.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f3e14006",
    "verify",
    "verify_f3e14006",
]
