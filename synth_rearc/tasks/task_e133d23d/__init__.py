from .generator import generate_e133d23d
from .verifier import verify_e133d23d


TASK_ID = "e133d23d"
generate = generate_e133d23d
verify = verify_e133d23d
REFERENCE_TASK_PATH = "data/official/arc2/training/e133d23d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e133d23d",
    "verify",
    "verify_e133d23d",
]
