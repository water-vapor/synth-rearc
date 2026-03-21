from .generator import generate_9c1e755f
from .verifier import verify_9c1e755f


TASK_ID = "9c1e755f"
generate = generate_9c1e755f
verify = verify_9c1e755f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9c1e755f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9c1e755f",
    "verify",
    "verify_9c1e755f",
]
