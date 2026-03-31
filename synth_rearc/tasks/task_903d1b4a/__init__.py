from .generator import generate_903d1b4a
from .verifier import verify_903d1b4a


TASK_ID = "903d1b4a"
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/903d1b4a.json"

generate = generate_903d1b4a
verify = verify_903d1b4a

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_903d1b4a",
    "verify",
    "verify_903d1b4a",
]
