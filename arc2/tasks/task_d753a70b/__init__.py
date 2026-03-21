from .generator import generate_d753a70b
from .verifier import verify_d753a70b


TASK_ID = "d753a70b"
generate = generate_d753a70b
verify = verify_d753a70b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d753a70b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d753a70b",
    "verify",
    "verify_d753a70b",
]
