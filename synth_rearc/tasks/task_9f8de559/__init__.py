from .generator import generate_9f8de559
from .verifier import verify_9f8de559


TASK_ID = "9f8de559"
generate = generate_9f8de559
verify = verify_9f8de559
REFERENCE_TASK_PATH = "data/official/arc2/training/9f8de559.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9f8de559",
    "verify",
    "verify_9f8de559",
]
