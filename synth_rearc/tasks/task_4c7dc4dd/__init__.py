from .generator import generate_4c7dc4dd
from .verifier import verify_4c7dc4dd


TASK_ID = "4c7dc4dd"
generate = generate_4c7dc4dd
verify = verify_4c7dc4dd
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/4c7dc4dd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4c7dc4dd",
    "verify",
    "verify_4c7dc4dd",
]
