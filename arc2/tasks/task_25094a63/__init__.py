from .generator import generate_25094a63
from .verifier import verify_25094a63


TASK_ID = "25094a63"
generate = generate_25094a63
verify = verify_25094a63
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/25094a63.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_25094a63",
    "verify",
    "verify_25094a63",
]
