from .generator import generate_0a1d4ef5
from .verifier import verify_0a1d4ef5


TASK_ID = "0a1d4ef5"
generate = generate_0a1d4ef5
verify = verify_0a1d4ef5
REFERENCE_TASK_PATH = "arc_original/evaluation/0a1d4ef5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_0a1d4ef5",
    "verify",
    "verify_0a1d4ef5",
]
