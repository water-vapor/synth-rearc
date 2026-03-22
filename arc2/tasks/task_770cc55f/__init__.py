from .generator import generate_770cc55f
from .verifier import verify_770cc55f


TASK_ID = "770cc55f"
generate = generate_770cc55f
verify = verify_770cc55f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/770cc55f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_770cc55f",
    "verify",
    "verify_770cc55f",
]
