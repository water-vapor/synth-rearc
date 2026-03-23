from .generator import generate_1d61978c
from .verifier import verify_1d61978c


TASK_ID = "1d61978c"
generate = generate_1d61978c
verify = verify_1d61978c
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1d61978c.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1d61978c",
    "verify",
    "verify_1d61978c",
]
