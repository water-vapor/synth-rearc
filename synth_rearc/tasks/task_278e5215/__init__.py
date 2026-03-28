from .generator import generate_278e5215
from .verifier import verify_278e5215


TASK_ID = "278e5215"
REFERENCE_TASK_PATH = "data/official/arc2/training/278e5215.json"

generate = generate_278e5215
verify = verify_278e5215

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_278e5215",
    "verify",
    "verify_278e5215",
]
