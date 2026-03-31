from .generator import generate_7666fa5d
from .verifier import verify_7666fa5d


TASK_ID = "7666fa5d"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/7666fa5d.json"

generate = generate_7666fa5d
verify = verify_7666fa5d

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7666fa5d",
    "verify",
    "verify_7666fa5d",
]
