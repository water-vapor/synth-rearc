from .generator import generate_516b51b7
from .verifier import verify_516b51b7


TASK_ID = "516b51b7"
generate = generate_516b51b7
verify = verify_516b51b7
REFERENCE_TASK_PATH = "data/official/arc2/training/516b51b7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_516b51b7",
    "verify",
    "verify_516b51b7",
]
