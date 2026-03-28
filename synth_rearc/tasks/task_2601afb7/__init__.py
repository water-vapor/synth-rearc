from .generator import generate_2601afb7
from .verifier import verify_2601afb7


TASK_ID = "2601afb7"
generate = generate_2601afb7
verify = verify_2601afb7
REFERENCE_TASK_PATH = "data/official/arc2/training/2601afb7.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2601afb7",
    "verify",
    "verify_2601afb7",
]
