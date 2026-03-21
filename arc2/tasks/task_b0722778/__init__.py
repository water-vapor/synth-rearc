from .generator import generate_b0722778
from .verifier import verify_b0722778


TASK_ID = "b0722778"
generate = generate_b0722778
verify = verify_b0722778
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b0722778.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b0722778",
    "verify",
    "verify_b0722778",
]
