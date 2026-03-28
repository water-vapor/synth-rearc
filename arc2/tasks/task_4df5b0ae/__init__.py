from .generator import generate_4df5b0ae
from .verifier import verify_4df5b0ae


TASK_ID = "4df5b0ae"
generate = generate_4df5b0ae
verify = verify_4df5b0ae
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4df5b0ae.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4df5b0ae",
    "verify",
    "verify_4df5b0ae",
]
