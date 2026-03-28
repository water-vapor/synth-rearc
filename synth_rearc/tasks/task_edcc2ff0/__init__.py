from .generator import generate_edcc2ff0
from .verifier import verify_edcc2ff0


TASK_ID = "edcc2ff0"
generate = generate_edcc2ff0
verify = verify_edcc2ff0
REFERENCE_TASK_PATH = "data/official/arc2/training/edcc2ff0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_edcc2ff0",
    "verify",
    "verify_edcc2ff0",
]
