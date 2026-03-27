from .generator import generate_337b420f
from .verifier import verify_337b420f


TASK_ID = "337b420f"
generate = generate_337b420f
verify = verify_337b420f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/337b420f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_337b420f",
    "verify",
    "verify_337b420f",
]
