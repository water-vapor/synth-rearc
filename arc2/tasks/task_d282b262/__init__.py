from .generator import generate_d282b262
from .verifier import verify_d282b262


TASK_ID = "d282b262"
generate = generate_d282b262
verify = verify_d282b262
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d282b262.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d282b262",
    "verify",
    "verify_d282b262",
]
