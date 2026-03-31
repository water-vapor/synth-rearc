from .generator import generate_b10624e5
from .verifier import verify_b10624e5


TASK_ID = "b10624e5"
generate = generate_b10624e5
verify = verify_b10624e5
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/b10624e5.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b10624e5",
    "verify",
    "verify_b10624e5",
]
