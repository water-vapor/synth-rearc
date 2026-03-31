from .generator import generate_4aab4007
from .verifier import verify_4aab4007


TASK_ID = "4aab4007"
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/4aab4007.json"

generate = generate_4aab4007
verify = verify_4aab4007

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4aab4007",
    "verify",
    "verify_4aab4007",
]
