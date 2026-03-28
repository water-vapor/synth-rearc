from .generator import generate_f3cdc58f
from .verifier import verify_f3cdc58f


TASK_ID = "f3cdc58f"
generate = generate_f3cdc58f
verify = verify_f3cdc58f
REFERENCE_TASK_PATH = "data/official/arc2/training/f3cdc58f.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f3cdc58f",
    "verify",
    "verify_f3cdc58f",
]
