from .generator import generate_52364a65
from .verifier import verify_52364a65


TASK_ID = "52364a65"
generate = generate_52364a65
verify = verify_52364a65
REFERENCE_TASK_PATH = "data/official/arc2/training/52364a65.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_52364a65",
    "verify",
    "verify_52364a65",
]
