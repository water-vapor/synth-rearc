from .generator import generate_21897d95
from .verifier import verify_21897d95


TASK_ID = "21897d95"
generate = generate_21897d95
verify = verify_21897d95
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/21897d95.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_21897d95",
    "verify",
    "verify_21897d95",
]
