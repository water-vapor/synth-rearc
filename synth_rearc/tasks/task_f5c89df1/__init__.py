from .generator import generate_f5c89df1
from .verifier import verify_f5c89df1


TASK_ID = "f5c89df1"
generate = generate_f5c89df1
verify = verify_f5c89df1
REFERENCE_TASK_PATH = "data/official/arc2/training/f5c89df1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f5c89df1",
    "verify",
    "verify_f5c89df1",
]
