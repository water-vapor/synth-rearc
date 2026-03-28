from .generator import generate_e4941b18
from .verifier import verify_e4941b18


TASK_ID = "e4941b18"
generate = generate_e4941b18
verify = verify_e4941b18
REFERENCE_TASK_PATH = "data/official/arc2/training/e4941b18.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e4941b18",
    "verify",
    "verify_e4941b18",
]
