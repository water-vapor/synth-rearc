from .generator import generate_c4d1a9ae
from .verifier import verify_c4d1a9ae


TASK_ID = "c4d1a9ae"
generate = generate_c4d1a9ae
verify = verify_c4d1a9ae
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/c4d1a9ae.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c4d1a9ae",
    "verify",
    "verify_c4d1a9ae",
]
