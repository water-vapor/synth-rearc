from .generator import generate_2697da3f
from .verifier import verify_2697da3f


TASK_ID = "2697da3f"
generate = generate_2697da3f
verify = verify_2697da3f
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/2697da3f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2697da3f",
    "verify",
    "verify_2697da3f",
]
