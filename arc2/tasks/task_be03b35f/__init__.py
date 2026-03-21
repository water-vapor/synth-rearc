from .generator import generate_be03b35f
from .verifier import verify_be03b35f


TASK_ID = "be03b35f"
generate = generate_be03b35f
verify = verify_be03b35f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/be03b35f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_be03b35f",
    "verify",
    "verify_be03b35f",
]
