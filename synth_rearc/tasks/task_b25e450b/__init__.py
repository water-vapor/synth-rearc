from .generator import generate_b25e450b
from .verifier import verify_b25e450b


TASK_ID = "b25e450b"
generate = generate_b25e450b
verify = verify_b25e450b
REFERENCE_TASK_PATH = "data/official/arc2/training/b25e450b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b25e450b",
    "verify",
    "verify_b25e450b",
]
