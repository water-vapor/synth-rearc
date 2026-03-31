from .generator import generate_7ed72f31
from .verifier import verify_7ed72f31


TASK_ID = "7ed72f31"
generate = generate_7ed72f31
verify = verify_7ed72f31
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/7ed72f31.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_7ed72f31",
    "verify",
    "verify_7ed72f31",
]
