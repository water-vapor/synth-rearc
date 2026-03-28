from .generator import generate_d37a1ef5
from .verifier import verify_d37a1ef5


TASK_ID = "d37a1ef5"
generate = generate_d37a1ef5
verify = verify_d37a1ef5
REFERENCE_TASK_PATH = "data/official/arc2/training/d37a1ef5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d37a1ef5",
    "verify",
    "verify_d37a1ef5",
]
