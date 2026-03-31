from .generator import generate_4c416de3
from .verifier import verify_4c416de3


TASK_ID = "4c416de3"
generate = generate_4c416de3
verify = verify_4c416de3
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/4c416de3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4c416de3",
    "verify",
    "verify_4c416de3",
]
