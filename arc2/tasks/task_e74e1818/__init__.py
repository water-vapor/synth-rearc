from .generator import generate_e74e1818
from .verifier import verify_e74e1818


TASK_ID = "e74e1818"
generate = generate_e74e1818
verify = verify_e74e1818
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e74e1818.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e74e1818",
    "verify",
    "verify_e74e1818",
]
