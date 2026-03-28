from .generator import generate_3f23242b
from .verifier import verify_3f23242b


TASK_ID = "3f23242b"
generate = generate_3f23242b
verify = verify_3f23242b
REFERENCE_TASK_PATH = "data/official/arc2/training/3f23242b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3f23242b",
    "verify",
    "verify_3f23242b",
]
