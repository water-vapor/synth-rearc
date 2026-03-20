from .generator import generate_1c56ad9f
from .verifier import verify_1c56ad9f


TASK_ID = "1c56ad9f"
generate = generate_1c56ad9f
verify = verify_1c56ad9f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1c56ad9f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1c56ad9f",
    "verify",
    "verify_1c56ad9f",
]
