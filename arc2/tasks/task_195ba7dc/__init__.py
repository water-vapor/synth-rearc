from .generator import generate_195ba7dc
from .verifier import verify_195ba7dc


TASK_ID = "195ba7dc"
generate = generate_195ba7dc
verify = verify_195ba7dc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/195ba7dc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_195ba7dc",
    "verify",
    "verify_195ba7dc",
]
