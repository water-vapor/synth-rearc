from .generator import generate_cd3c21df
from .verifier import verify_cd3c21df


TASK_ID = "cd3c21df"
generate = generate_cd3c21df
verify = verify_cd3c21df
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/cd3c21df.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cd3c21df",
    "verify",
    "verify_cd3c21df",
]
