from .generator import generate_aa18de87
from .verifier import verify_aa18de87


TASK_ID = "aa18de87"
generate = generate_aa18de87
verify = verify_aa18de87
REFERENCE_TASK_PATH = "data/official/arc2/training/aa18de87.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_aa18de87",
    "verify",
    "verify_aa18de87",
]
