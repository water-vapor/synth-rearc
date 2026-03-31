from .generator import generate_8f3a5a89
from .verifier import verify_8f3a5a89


TASK_ID = "8f3a5a89"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/8f3a5a89.json"

generate = generate_8f3a5a89
verify = verify_8f3a5a89

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8f3a5a89",
    "verify",
    "verify_8f3a5a89",
]
