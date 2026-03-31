from .generator import generate_d59b0160
from .verifier import verify_d59b0160


TASK_ID = "d59b0160"
generate = generate_d59b0160
verify = verify_d59b0160
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/d59b0160.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d59b0160",
    "verify",
    "verify_d59b0160",
]
