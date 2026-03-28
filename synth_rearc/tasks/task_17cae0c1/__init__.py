from .generator import generate_17cae0c1
from .verifier import verify_17cae0c1


TASK_ID = "17cae0c1"
generate = generate_17cae0c1
verify = verify_17cae0c1
REFERENCE_TASK_PATH = "data/official/arc2/training/17cae0c1.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_17cae0c1",
    "verify",
    "verify_17cae0c1",
]
