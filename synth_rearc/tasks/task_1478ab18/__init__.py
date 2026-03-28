from .generator import generate_1478ab18
from .verifier import verify_1478ab18


TASK_ID = "1478ab18"
generate = generate_1478ab18
verify = verify_1478ab18
REFERENCE_TASK_PATH = "data/official/arc2/training/1478ab18.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1478ab18",
    "verify",
    "verify_1478ab18",
]
