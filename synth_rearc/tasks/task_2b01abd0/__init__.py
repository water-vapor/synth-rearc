from .generator import generate_2b01abd0
from .verifier import verify_2b01abd0


TASK_ID = "2b01abd0"
generate = generate_2b01abd0
verify = verify_2b01abd0
REFERENCE_TASK_PATH = "data/official/arc2/training/2b01abd0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2b01abd0",
    "verify",
    "verify_2b01abd0",
]
