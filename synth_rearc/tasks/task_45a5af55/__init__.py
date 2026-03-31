from .generator import generate_45a5af55
from .verifier import verify_45a5af55


TASK_ID = "45a5af55"
generate = generate_45a5af55
verify = verify_45a5af55
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/45a5af55.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_45a5af55",
    "verify",
    "verify_45a5af55",
]
