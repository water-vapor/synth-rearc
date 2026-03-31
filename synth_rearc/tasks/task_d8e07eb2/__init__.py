from .generator import generate_d8e07eb2
from .verifier import verify_d8e07eb2


TASK_ID = "d8e07eb2"
generate = generate_d8e07eb2
verify = verify_d8e07eb2
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/d8e07eb2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d8e07eb2",
    "verify",
    "verify_d8e07eb2",
]
