from .generator import generate_a8610ef7
from .verifier import verify_a8610ef7


TASK_ID = "a8610ef7"
generate = generate_a8610ef7
verify = verify_a8610ef7
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a8610ef7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a8610ef7",
    "verify",
    "verify_a8610ef7",
]
