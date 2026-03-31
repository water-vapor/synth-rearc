from .generator import generate_8e5c0c38
from .verifier import verify_8e5c0c38


TASK_ID = "8e5c0c38"
generate = generate_8e5c0c38
verify = verify_8e5c0c38
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/8e5c0c38.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8e5c0c38",
    "verify",
    "verify_8e5c0c38",
]
