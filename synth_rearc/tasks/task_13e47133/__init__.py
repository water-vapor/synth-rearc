from .generator import generate_13e47133
from .verifier import verify_13e47133


TASK_ID = "13e47133"
generate = generate_13e47133
verify = verify_13e47133
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/13e47133.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_13e47133",
    "verify",
    "verify_13e47133",
]
