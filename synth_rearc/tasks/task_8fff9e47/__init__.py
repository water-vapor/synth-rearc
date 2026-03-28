from .generator import generate_8fff9e47
from .verifier import verify_8fff9e47


TASK_ID = "8fff9e47"
generate = generate_8fff9e47
verify = verify_8fff9e47
REFERENCE_TASK_PATH = "data/official/arc2/training/8fff9e47.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8fff9e47",
    "verify",
    "verify_8fff9e47",
]
