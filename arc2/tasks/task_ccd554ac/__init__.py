from .generator import generate_ccd554ac
from .verifier import verify_ccd554ac


TASK_ID = "ccd554ac"
generate = generate_ccd554ac
verify = verify_ccd554ac
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ccd554ac.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ccd554ac",
    "verify",
    "verify_ccd554ac",
]
