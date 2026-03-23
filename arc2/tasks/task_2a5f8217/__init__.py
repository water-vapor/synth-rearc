from .generator import generate_2a5f8217
from .verifier import verify_2a5f8217


TASK_ID = "2a5f8217"
generate = generate_2a5f8217
verify = verify_2a5f8217
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/2a5f8217.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2a5f8217",
    "verify",
    "verify_2a5f8217",
]
