from .generator import generate_f0f8a26d
from .verifier import verify_f0f8a26d


TASK_ID = "f0f8a26d"
generate = generate_f0f8a26d
verify = verify_f0f8a26d
REFERENCE_TASK_PATH = "data/official/arc2/training/f0f8a26d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f0f8a26d",
    "verify",
    "verify_f0f8a26d",
]
