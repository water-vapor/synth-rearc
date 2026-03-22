from .generator import generate_8dae5dfc
from .verifier import verify_8dae5dfc


TASK_ID = "8dae5dfc"
generate = generate_8dae5dfc
verify = verify_8dae5dfc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/8dae5dfc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8dae5dfc",
    "verify",
    "verify_8dae5dfc",
]
