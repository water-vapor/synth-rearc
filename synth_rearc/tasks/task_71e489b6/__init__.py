from .generator import generate_71e489b6
from .verifier import verify_71e489b6


TASK_ID = "71e489b6"
generate = generate_71e489b6
verify = verify_71e489b6
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/71e489b6.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_71e489b6",
    "verify",
    "verify_71e489b6",
]
