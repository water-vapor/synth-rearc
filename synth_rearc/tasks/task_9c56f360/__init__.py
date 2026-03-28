from .generator import generate_9c56f360
from .verifier import verify_9c56f360


TASK_ID = "9c56f360"
generate = generate_9c56f360
verify = verify_9c56f360
REFERENCE_TASK_PATH = "data/official/arc2/training/9c56f360.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9c56f360",
    "verify",
    "verify_9c56f360",
]
