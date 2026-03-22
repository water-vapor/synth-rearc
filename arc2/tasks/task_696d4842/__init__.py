from .generator import generate_696d4842
from .verifier import verify_696d4842


TASK_ID = "696d4842"
generate = generate_696d4842
verify = verify_696d4842
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/696d4842.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_696d4842",
    "verify",
    "verify_696d4842",
]
