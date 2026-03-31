from .generator import generate_8b9c3697
from .verifier import verify_8b9c3697


TASK_ID = "8b9c3697"
generate = generate_8b9c3697
verify = verify_8b9c3697
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/8b9c3697.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8b9c3697",
    "verify",
    "verify_8b9c3697",
]
