from .generator import generate_2b83f449
from .verifier import verify_2b83f449


TASK_ID = "2b83f449"
generate = generate_2b83f449
verify = verify_2b83f449
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/2b83f449.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2b83f449",
    "verify",
    "verify_2b83f449",
]
