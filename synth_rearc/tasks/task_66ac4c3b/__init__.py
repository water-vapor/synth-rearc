from .generator import generate_66ac4c3b
from .verifier import verify_66ac4c3b


TASK_ID = "66ac4c3b"
generate = generate_66ac4c3b
verify = verify_66ac4c3b
REFERENCE_TASK_PATH = "data/official/arc2/training/66ac4c3b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_66ac4c3b",
    "verify",
    "verify_66ac4c3b",
]
