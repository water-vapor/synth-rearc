from .generator import generate_5ecac7f7
from .verifier import verify_5ecac7f7


TASK_ID = "5ecac7f7"
generate = generate_5ecac7f7
verify = verify_5ecac7f7
REFERENCE_TASK_PATH = "data/official/arc2/training/5ecac7f7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5ecac7f7",
    "verify",
    "verify_5ecac7f7",
]
