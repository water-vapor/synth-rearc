from .generator import generate_0692e18c
from .verifier import verify_0692e18c


TASK_ID = "0692e18c"
generate = generate_0692e18c
verify = verify_0692e18c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/0692e18c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0692e18c",
    "verify",
    "verify_0692e18c",
]
