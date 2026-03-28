from .generator import generate_81c0276b
from .verifier import verify_81c0276b


TASK_ID = "81c0276b"
generate = generate_81c0276b
verify = verify_81c0276b
REFERENCE_TASK_PATH = "data/official/arc2/training/81c0276b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_81c0276b",
    "verify",
    "verify_81c0276b",
]
