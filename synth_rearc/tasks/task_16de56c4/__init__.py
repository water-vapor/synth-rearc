from .generator import generate_16de56c4
from .verifier import verify_16de56c4


TASK_ID = "16de56c4"
generate = generate_16de56c4
verify = verify_16de56c4
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/16de56c4.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_16de56c4",
    "verify",
    "verify_16de56c4",
]
