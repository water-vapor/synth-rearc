from .generator import generate_31adaf00
from .verifier import verify_31adaf00


TASK_ID = "31adaf00"
generate = generate_31adaf00
verify = verify_31adaf00
REFERENCE_TASK_PATH = "data/official/arc2/training/31adaf00.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_31adaf00",
    "verify",
    "verify_31adaf00",
]
