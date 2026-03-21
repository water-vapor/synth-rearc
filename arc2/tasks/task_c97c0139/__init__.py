from .generator import generate_c97c0139
from .verifier import verify_c97c0139


TASK_ID = "c97c0139"
generate = generate_c97c0139
verify = verify_c97c0139
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/c97c0139.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c97c0139",
    "verify",
    "verify_c97c0139",
]
