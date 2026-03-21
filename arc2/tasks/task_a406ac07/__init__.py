from .generator import generate_a406ac07
from .verifier import verify_a406ac07


TASK_ID = "a406ac07"
generate = generate_a406ac07
verify = verify_a406ac07
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a406ac07.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a406ac07",
    "verify",
    "verify_a406ac07",
]
