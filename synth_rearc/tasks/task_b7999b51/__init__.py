from .generator import generate_b7999b51
from .verifier import verify_b7999b51


TASK_ID = "b7999b51"
generate = generate_b7999b51
verify = verify_b7999b51
REFERENCE_TASK_PATH = "data/official/arc2/training/b7999b51.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b7999b51",
    "verify",
    "verify_b7999b51",
]
