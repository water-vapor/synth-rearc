from .generator import generate_4f537728
from .verifier import verify_4f537728


TASK_ID = "4f537728"
generate = generate_4f537728
verify = verify_4f537728
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4f537728.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4f537728",
    "verify",
    "verify_4f537728",
]
