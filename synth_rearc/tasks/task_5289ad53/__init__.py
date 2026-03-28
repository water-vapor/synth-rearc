from .generator import generate_5289ad53
from .verifier import verify_5289ad53


TASK_ID = "5289ad53"
generate = generate_5289ad53
verify = verify_5289ad53
REFERENCE_TASK_PATH = "data/official/arc2/training/5289ad53.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5289ad53",
    "verify",
    "verify_5289ad53",
]
