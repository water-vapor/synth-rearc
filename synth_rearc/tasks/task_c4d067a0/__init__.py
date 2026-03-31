from .generator import generate_c4d067a0
from .verifier import verify_c4d067a0


TASK_ID = "c4d067a0"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/c4d067a0.json"

generate = generate_c4d067a0
verify = verify_c4d067a0

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c4d067a0",
    "verify",
    "verify_c4d067a0",
]
