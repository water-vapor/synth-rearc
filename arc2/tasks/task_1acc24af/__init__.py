from .generator import generate_1acc24af
from .verifier import verify_1acc24af


TASK_ID = "1acc24af"
generate = generate_1acc24af
verify = verify_1acc24af
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1acc24af.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1acc24af",
    "verify",
    "verify_1acc24af",
]
