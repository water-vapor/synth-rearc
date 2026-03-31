from .generator import generate_4c3d4a41
from .verifier import verify_4c3d4a41


TASK_ID = "4c3d4a41"
generate = generate_4c3d4a41
verify = verify_4c3d4a41
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/4c3d4a41.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4c3d4a41",
    "verify",
    "verify_4c3d4a41",
]
