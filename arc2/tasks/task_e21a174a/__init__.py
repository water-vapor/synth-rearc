from .generator import generate_e21a174a
from .verifier import verify_e21a174a


TASK_ID = "e21a174a"
generate = generate_e21a174a
verify = verify_e21a174a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e21a174a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e21a174a",
    "verify",
    "verify_e21a174a",
]
