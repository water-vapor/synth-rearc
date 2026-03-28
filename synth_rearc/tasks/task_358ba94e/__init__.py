from .generator import generate_358ba94e
from .verifier import verify_358ba94e


TASK_ID = "358ba94e"
generate = generate_358ba94e
verify = verify_358ba94e
REFERENCE_TASK_PATH = "data/official/arc2/training/358ba94e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_358ba94e",
    "verify",
    "verify_358ba94e",
]
