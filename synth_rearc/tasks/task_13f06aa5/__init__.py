from .generator import generate_13f06aa5
from .verifier import verify_13f06aa5


TASK_ID = "13f06aa5"
generate = generate_13f06aa5
verify = verify_13f06aa5
REFERENCE_TASK_PATH = "data/official/arc2/training/13f06aa5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_13f06aa5",
    "verify",
    "verify_13f06aa5",
]
