from .generator import generate_902510d5
from .verifier import verify_902510d5


TASK_ID = "902510d5"
generate = generate_902510d5
verify = verify_902510d5
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/902510d5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_902510d5",
    "verify",
    "verify_902510d5",
]
