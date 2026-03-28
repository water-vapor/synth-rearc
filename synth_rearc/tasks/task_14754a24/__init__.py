from .generator import generate_14754a24
from .verifier import verify_14754a24


TASK_ID = "14754a24"
generate = generate_14754a24
verify = verify_14754a24
REFERENCE_TASK_PATH = "data/official/arc2/training/14754a24.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_14754a24",
    "verify",
    "verify_14754a24",
]
