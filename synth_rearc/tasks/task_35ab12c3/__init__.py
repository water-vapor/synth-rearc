from .generator import generate_35ab12c3
from .verifier import verify_35ab12c3


TASK_ID = "35ab12c3"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/35ab12c3.json"

generate = generate_35ab12c3
verify = verify_35ab12c3

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_35ab12c3",
    "verify",
    "verify_35ab12c3",
]
