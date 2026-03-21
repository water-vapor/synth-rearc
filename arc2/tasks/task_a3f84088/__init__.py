from .generator import generate_a3f84088
from .verifier import verify_a3f84088


TASK_ID = "a3f84088"
generate = generate_a3f84088
verify = verify_a3f84088
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/a3f84088.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a3f84088",
    "verify",
    "verify_a3f84088",
]
