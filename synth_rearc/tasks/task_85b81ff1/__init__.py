from .generator import generate_85b81ff1
from .verifier import verify_85b81ff1


TASK_ID = "85b81ff1"
generate = generate_85b81ff1
verify = verify_85b81ff1
REFERENCE_TASK_PATH = "data/official/arc2/training/85b81ff1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_85b81ff1",
    "verify",
    "verify_85b81ff1",
]
