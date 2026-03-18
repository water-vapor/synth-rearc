from .generator import generate_fea12743
from .verifier import verify_fea12743


TASK_ID = "fea12743"
generate = generate_fea12743
verify = verify_fea12743
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/fea12743.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_fea12743",
    "verify",
    "verify_fea12743",
]
