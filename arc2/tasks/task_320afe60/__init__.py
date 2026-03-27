from .generator import generate_320afe60
from .verifier import verify_320afe60


TASK_ID = "320afe60"
generate = generate_320afe60
verify = verify_320afe60
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/320afe60.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_320afe60",
    "verify",
    "verify_320afe60",
]
