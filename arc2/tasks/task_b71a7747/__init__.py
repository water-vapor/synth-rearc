from .generator import generate_b71a7747
from .verifier import verify_b71a7747


TASK_ID = "b71a7747"
generate = generate_b71a7747
verify = verify_b71a7747
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b71a7747.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b71a7747",
    "verify",
    "verify_b71a7747",
]
