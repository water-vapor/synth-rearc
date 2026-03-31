from .generator import generate_221dfab4
from .verifier import verify_221dfab4


TASK_ID = "221dfab4"
generate = generate_221dfab4
verify = verify_221dfab4
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/221dfab4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_221dfab4",
    "verify",
    "verify_221dfab4",
]
