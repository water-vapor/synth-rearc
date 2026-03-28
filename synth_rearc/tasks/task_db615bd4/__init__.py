from .generator import generate_db615bd4
from .verifier import verify_db615bd4


TASK_ID = "db615bd4"
generate = generate_db615bd4
verify = verify_db615bd4
REFERENCE_TASK_PATH = "data/official/arc2/training/db615bd4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_db615bd4",
    "verify",
    "verify_db615bd4",
]
