from .generator import generate_3d6c6e23
from .verifier import verify_3d6c6e23


TASK_ID = "3d6c6e23"
generate = generate_3d6c6e23
verify = verify_3d6c6e23
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/3d6c6e23.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3d6c6e23",
    "verify",
    "verify_3d6c6e23",
]
