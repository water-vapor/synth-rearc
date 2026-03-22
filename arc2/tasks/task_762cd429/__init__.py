from .generator import generate_762cd429
from .verifier import verify_762cd429


TASK_ID = "762cd429"
generate = generate_762cd429
verify = verify_762cd429
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/762cd429.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_762cd429",
    "verify",
    "verify_762cd429",
]
