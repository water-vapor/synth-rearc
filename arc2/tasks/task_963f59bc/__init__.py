from .generator import generate_963f59bc
from .verifier import verify_963f59bc


TASK_ID = "963f59bc"
generate = generate_963f59bc
verify = verify_963f59bc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/963f59bc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_963f59bc",
    "verify",
    "verify_963f59bc",
]
