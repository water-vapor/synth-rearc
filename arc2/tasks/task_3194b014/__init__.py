from .generator import generate_3194b014
from .verifier import verify_3194b014


TASK_ID = "3194b014"
generate = generate_3194b014
verify = verify_3194b014
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/3194b014.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3194b014",
    "verify",
    "verify_3194b014",
]
