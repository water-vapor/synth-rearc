from .generator import generate_142ca369
from .verifier import verify_142ca369


TASK_ID = "142ca369"
generate = generate_142ca369
verify = verify_142ca369
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/142ca369.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_142ca369",
    "verify",
    "verify_142ca369",
]
