from .generator import generate_f5aa3634
from .verifier import verify_f5aa3634


TASK_ID = "f5aa3634"
generate = generate_f5aa3634
verify = verify_f5aa3634
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f5aa3634.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f5aa3634",
    "verify",
    "verify_f5aa3634",
]
