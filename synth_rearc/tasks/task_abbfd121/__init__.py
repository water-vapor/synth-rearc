from .generator import generate_abbfd121
from .verifier import verify_abbfd121


TASK_ID = "abbfd121"
generate = generate_abbfd121
verify = verify_abbfd121
REFERENCE_TASK_PATH = "data/official/arc2/training/abbfd121.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_abbfd121",
    "verify",
    "verify_abbfd121",
]
