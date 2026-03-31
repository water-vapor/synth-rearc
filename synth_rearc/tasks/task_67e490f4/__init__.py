from .generator import generate_67e490f4
from .verifier import verify_67e490f4


TASK_ID = "67e490f4"
generate = generate_67e490f4
verify = verify_67e490f4
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/67e490f4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_67e490f4",
    "verify",
    "verify_67e490f4",
]
