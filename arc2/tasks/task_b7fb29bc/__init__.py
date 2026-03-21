from .generator import generate_b7fb29bc
from .verifier import verify_b7fb29bc


TASK_ID = "b7fb29bc"
generate = generate_b7fb29bc
verify = verify_b7fb29bc
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b7fb29bc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b7fb29bc",
    "verify",
    "verify_b7fb29bc",
]
