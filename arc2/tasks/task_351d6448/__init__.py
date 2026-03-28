from .generator import generate_351d6448
from .verifier import verify_351d6448


TASK_ID = "351d6448"
generate = generate_351d6448
verify = verify_351d6448
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/351d6448.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_351d6448",
    "verify",
    "verify_351d6448",
]
