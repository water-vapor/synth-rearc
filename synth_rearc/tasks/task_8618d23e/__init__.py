from .generator import generate_8618d23e
from .verifier import verify_8618d23e


TASK_ID = "8618d23e"
generate = generate_8618d23e
verify = verify_8618d23e
REFERENCE_TASK_PATH = "data/official/arc2/training/8618d23e.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8618d23e",
    "verify",
    "verify_8618d23e",
]
