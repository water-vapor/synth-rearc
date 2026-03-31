from .generator import generate_b9e38dc0
from .verifier import verify_b9e38dc0


TASK_ID = "b9e38dc0"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/b9e38dc0.json"

generate = generate_b9e38dc0
verify = verify_b9e38dc0

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b9e38dc0",
    "verify",
    "verify_b9e38dc0",
]
