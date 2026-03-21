from .generator import generate_baf41dbf
from .verifier import verify_baf41dbf


TASK_ID = "baf41dbf"
generate = generate_baf41dbf
verify = verify_baf41dbf
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/baf41dbf.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_baf41dbf",
    "verify",
    "verify_baf41dbf",
]
