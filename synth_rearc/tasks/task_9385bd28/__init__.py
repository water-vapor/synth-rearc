from .generator import generate_9385bd28
from .verifier import verify_9385bd28


TASK_ID = "9385bd28"
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/9385bd28.json"

generate = generate_9385bd28
verify = verify_9385bd28

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9385bd28",
    "verify",
    "verify_9385bd28",
]
