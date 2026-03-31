from .generator import generate_8698868d
from .verifier import verify_8698868d


TASK_ID = "8698868d"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/8698868d.json"

generate = generate_8698868d
verify = verify_8698868d

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8698868d",
    "verify",
    "verify_8698868d",
]
