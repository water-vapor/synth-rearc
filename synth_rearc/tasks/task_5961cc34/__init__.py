from .generator import generate_5961cc34
from .verifier import verify_5961cc34


TASK_ID = "5961cc34"
generate = generate_5961cc34
verify = verify_5961cc34
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/5961cc34.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5961cc34",
    "verify",
    "verify_5961cc34",
]
