from .generator import generate_1ae2feb7
from .verifier import verify_1ae2feb7


TASK_ID = "1ae2feb7"
generate = generate_1ae2feb7
verify = verify_1ae2feb7
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/1ae2feb7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1ae2feb7",
    "verify",
    "verify_1ae2feb7",
]
