from .generator import generate_281123b4
from .verifier import verify_281123b4


TASK_ID = "281123b4"
generate = generate_281123b4
verify = verify_281123b4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/281123b4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_281123b4",
    "verify",
    "verify_281123b4",
]
