from .generator import generate_2f0c5170
from .verifier import verify_2f0c5170


TASK_ID = "2f0c5170"
generate = generate_2f0c5170
verify = verify_2f0c5170
REFERENCE_TASK_PATH = "data/official/arc2/training/2f0c5170.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2f0c5170",
    "verify",
    "verify_2f0c5170",
]
