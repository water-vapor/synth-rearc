from .generator import generate_3e6067c3
from .verifier import verify_3e6067c3


TASK_ID = "3e6067c3"
generate = generate_3e6067c3
verify = verify_3e6067c3
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/3e6067c3.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_3e6067c3",
    "verify",
    "verify_3e6067c3",
]
