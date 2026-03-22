from .generator import generate_833dafe3
from .verifier import verify_833dafe3


TASK_ID = "833dafe3"
generate = generate_833dafe3
verify = verify_833dafe3
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/833dafe3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_833dafe3",
    "verify",
    "verify_833dafe3",
]
