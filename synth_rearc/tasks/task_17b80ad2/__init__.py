from .generator import generate_17b80ad2
from .verifier import verify_17b80ad2


TASK_ID = "17b80ad2"
generate = generate_17b80ad2
verify = verify_17b80ad2
REFERENCE_TASK_PATH = "data/official/arc2/training/17b80ad2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_17b80ad2",
    "verify",
    "verify_17b80ad2",
]
