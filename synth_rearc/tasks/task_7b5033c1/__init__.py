from .generator import generate_7b5033c1
from .verifier import verify_7b5033c1


TASK_ID = "7b5033c1"
generate = generate_7b5033c1
verify = verify_7b5033c1
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/7b5033c1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7b5033c1",
    "verify",
    "verify_7b5033c1",
]
