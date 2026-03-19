from .generator import generate_e57337a4
from .verifier import verify_e57337a4


TASK_ID = "e57337a4"
generate = generate_e57337a4
verify = verify_e57337a4
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e57337a4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e57337a4",
    "verify",
    "verify_e57337a4",
]
