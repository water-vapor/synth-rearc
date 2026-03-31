from .generator import generate_2ba387bc
from .verifier import verify_2ba387bc


TASK_ID = "2ba387bc"
generate = generate_2ba387bc
verify = verify_2ba387bc
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/2ba387bc.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2ba387bc",
    "verify",
    "verify_2ba387bc",
]
