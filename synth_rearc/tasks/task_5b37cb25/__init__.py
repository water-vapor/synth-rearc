from .generator import generate_5b37cb25
from .verifier import verify_5b37cb25


TASK_ID = "5b37cb25"
generate = generate_5b37cb25
verify = verify_5b37cb25
REFERENCE_TASK_PATH = "data/official/arc2/training/5b37cb25.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5b37cb25",
    "verify",
    "verify_5b37cb25",
]
