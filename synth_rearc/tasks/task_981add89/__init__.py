from .generator import generate_981add89
from .verifier import verify_981add89


TASK_ID = "981add89"
generate = generate_981add89
verify = verify_981add89
REFERENCE_TASK_PATH = "data/official/arc2/training/981add89.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_981add89",
    "verify",
    "verify_981add89",
]
