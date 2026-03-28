from .generator import generate_575b1a71
from .verifier import verify_575b1a71


TASK_ID = "575b1a71"
generate = generate_575b1a71
verify = verify_575b1a71
REFERENCE_TASK_PATH = "data/official/arc2/training/575b1a71.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_575b1a71",
    "verify",
    "verify_575b1a71",
]
