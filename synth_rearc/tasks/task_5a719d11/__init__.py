from .generator import generate_5a719d11
from .verifier import verify_5a719d11


TASK_ID = "5a719d11"
generate = generate_5a719d11
verify = verify_5a719d11
REFERENCE_TASK_PATH = "data/official/arc2/training/5a719d11.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5a719d11",
    "verify",
    "verify_5a719d11",
]
