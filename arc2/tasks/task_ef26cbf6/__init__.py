from .generator import generate_ef26cbf6
from .verifier import verify_ef26cbf6


TASK_ID = "ef26cbf6"
generate = generate_ef26cbf6
verify = verify_ef26cbf6
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ef26cbf6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ef26cbf6",
    "verify",
    "verify_ef26cbf6",
]
