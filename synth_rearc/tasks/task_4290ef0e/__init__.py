from .generator import generate_4290ef0e
from .verifier import verify_4290ef0e


TASK_ID = "4290ef0e"
generate = generate_4290ef0e
verify = verify_4290ef0e
REFERENCE_TASK_PATH = "data/official/arc1/training/4290ef0e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4290ef0e",
    "verify",
    "verify_4290ef0e",
]
