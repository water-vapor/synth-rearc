from .generator import generate_48f8583b
from .verifier import verify_48f8583b


TASK_ID = "48f8583b"
generate = generate_48f8583b
verify = verify_48f8583b
REFERENCE_TASK_PATH = "data/official/arc2/training/48f8583b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_48f8583b",
    "verify",
    "verify_48f8583b",
]
