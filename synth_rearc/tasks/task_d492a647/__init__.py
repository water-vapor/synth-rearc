from .generator import generate_d492a647
from .verifier import verify_d492a647


TASK_ID = "d492a647"
generate = generate_d492a647
verify = verify_d492a647
REFERENCE_TASK_PATH = "data/official/arc2/training/d492a647.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d492a647",
    "verify",
    "verify_d492a647",
]
