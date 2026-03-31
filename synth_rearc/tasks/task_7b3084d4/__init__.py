from .generator import generate_7b3084d4
from .verifier import verify_7b3084d4


TASK_ID = "7b3084d4"
generate = generate_7b3084d4
verify = verify_7b3084d4
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/7b3084d4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7b3084d4",
    "verify",
    "verify_7b3084d4",
]
