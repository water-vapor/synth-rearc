from .generator import generate_cc9053aa
from .verifier import verify_cc9053aa


TASK_ID = "cc9053aa"
generate = generate_cc9053aa
verify = verify_cc9053aa
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/cc9053aa.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cc9053aa",
    "verify",
    "verify_cc9053aa",
]
