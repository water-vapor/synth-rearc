from .generator import generate_f3b10344
from .verifier import verify_f3b10344


TASK_ID = "f3b10344"
generate = generate_f3b10344
verify = verify_f3b10344
REFERENCE_TASK_PATH = "data/official/arc2/training/f3b10344.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f3b10344",
    "verify",
    "verify_f3b10344",
]
