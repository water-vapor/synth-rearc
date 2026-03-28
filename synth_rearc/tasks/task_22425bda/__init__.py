from .generator import generate_22425bda
from .verifier import verify_22425bda


TASK_ID = "22425bda"
generate = generate_22425bda
verify = verify_22425bda
REFERENCE_TASK_PATH = "data/official/arc2/training/22425bda.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_22425bda",
    "verify",
    "verify_22425bda",
]
