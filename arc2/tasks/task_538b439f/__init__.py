from .generator import generate_538b439f
from .verifier import verify_538b439f


TASK_ID = "538b439f"
generate = generate_538b439f
verify = verify_538b439f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/538b439f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_538b439f",
    "verify",
    "verify_538b439f",
]
