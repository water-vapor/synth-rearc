from .generator import generate_e619ca6e
from .verifier import verify_e619ca6e


TASK_ID = "e619ca6e"
generate = generate_e619ca6e
verify = verify_e619ca6e
REFERENCE_TASK_PATH = "data/official/arc2/training/e619ca6e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e619ca6e",
    "verify",
    "verify_e619ca6e",
]
