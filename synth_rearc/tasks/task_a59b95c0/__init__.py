from .generator import generate_a59b95c0
from .verifier import verify_a59b95c0


TASK_ID = "a59b95c0"
generate = generate_a59b95c0
verify = verify_a59b95c0
REFERENCE_TASK_PATH = "data/official/arc2/training/a59b95c0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_a59b95c0",
    "verify",
    "verify_a59b95c0",
]
