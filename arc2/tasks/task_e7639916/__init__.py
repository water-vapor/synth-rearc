from .generator import generate_e7639916
from .verifier import verify_e7639916


TASK_ID = "e7639916"
generate = generate_e7639916
verify = verify_e7639916
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e7639916.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e7639916",
    "verify",
    "verify_e7639916",
]
