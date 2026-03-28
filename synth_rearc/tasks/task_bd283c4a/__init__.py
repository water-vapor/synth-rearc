from .generator import generate_bd283c4a
from .verifier import verify_bd283c4a


TASK_ID = "bd283c4a"
generate = generate_bd283c4a
verify = verify_bd283c4a
REFERENCE_TASK_PATH = "data/official/arc2/training/bd283c4a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bd283c4a",
    "verify",
    "verify_bd283c4a",
]
