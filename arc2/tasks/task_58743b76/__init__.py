from .generator import generate_58743b76
from .verifier import verify_58743b76


TASK_ID = "58743b76"
generate = generate_58743b76
verify = verify_58743b76
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/58743b76.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_58743b76",
    "verify",
    "verify_58743b76",
]
