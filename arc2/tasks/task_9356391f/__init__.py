from .generator import generate_9356391f
from .verifier import verify_9356391f


TASK_ID = "9356391f"
generate = generate_9356391f
verify = verify_9356391f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9356391f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9356391f",
    "verify",
    "verify_9356391f",
]
