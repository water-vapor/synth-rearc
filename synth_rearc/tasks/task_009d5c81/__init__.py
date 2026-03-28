from .generator import generate_009d5c81
from .verifier import verify_009d5c81


TASK_ID = "009d5c81"
generate = generate_009d5c81
verify = verify_009d5c81
REFERENCE_TASK_PATH = "data/official/arc2/training/009d5c81.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_009d5c81",
    "verify",
    "verify_009d5c81",
]
