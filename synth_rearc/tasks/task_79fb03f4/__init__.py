from .generator import generate_79fb03f4
from .verifier import verify_79fb03f4


TASK_ID = "79fb03f4"
generate = generate_79fb03f4
verify = verify_79fb03f4
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/79fb03f4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_79fb03f4",
    "verify",
    "verify_79fb03f4",
]
