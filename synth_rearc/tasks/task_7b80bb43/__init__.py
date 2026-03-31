from .generator import generate_7b80bb43
from .verifier import verify_7b80bb43


TASK_ID = "7b80bb43"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/7b80bb43.json"

generate = generate_7b80bb43
verify = verify_7b80bb43

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7b80bb43",
    "verify",
    "verify_7b80bb43",
]
