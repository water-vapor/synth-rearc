from .generator import generate_4c177718
from .verifier import verify_4c177718


TASK_ID = "4c177718"
generate = generate_4c177718
verify = verify_4c177718
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4c177718.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4c177718",
    "verify",
    "verify_4c177718",
]
