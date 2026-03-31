from .generator import generate_271d71e2
from .verifier import verify_271d71e2


TASK_ID = "271d71e2"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/271d71e2.json"

generate = generate_271d71e2
verify = verify_271d71e2

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_271d71e2",
    "verify",
    "verify_271d71e2",
]
