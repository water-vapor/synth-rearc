from .generator import generate_42a15761
from .verifier import verify_42a15761


TASK_ID = "42a15761"
generate = generate_42a15761
verify = verify_42a15761
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/42a15761.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_42a15761",
    "verify",
    "verify_42a15761",
]
