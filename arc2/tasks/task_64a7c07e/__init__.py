from .generator import generate_64a7c07e
from .verifier import verify_64a7c07e


TASK_ID = "64a7c07e"
generate = generate_64a7c07e
verify = verify_64a7c07e
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/64a7c07e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_64a7c07e",
    "verify",
    "verify_64a7c07e",
]
