from .generator import generate_8abad3cf
from .verifier import verify_8abad3cf


TASK_ID = "8abad3cf"
generate = generate_8abad3cf
verify = verify_8abad3cf
REFERENCE_TASK_PATH = "data/official/arc2/training/8abad3cf.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8abad3cf",
    "verify",
    "verify_8abad3cf",
]
