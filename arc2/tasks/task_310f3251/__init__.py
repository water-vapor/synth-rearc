from .generator import generate_310f3251
from .verifier import verify_310f3251


TASK_ID = "310f3251"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/310f3251.json"

generate = generate_310f3251
verify = verify_310f3251

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_310f3251",
    "verify",
    "verify_310f3251",
]
