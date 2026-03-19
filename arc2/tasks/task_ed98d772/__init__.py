from .generator import generate_ed98d772
from .verifier import verify_ed98d772


TASK_ID = "ed98d772"
generate = generate_ed98d772
verify = verify_ed98d772
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ed98d772.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ed98d772",
    "verify",
    "verify_ed98d772",
]
