from .generator import generate_291dc1e1
from .verifier import verify_291dc1e1


TASK_ID = "291dc1e1"
generate = generate_291dc1e1
verify = verify_291dc1e1
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/291dc1e1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_291dc1e1",
    "verify",
    "verify_291dc1e1",
]
