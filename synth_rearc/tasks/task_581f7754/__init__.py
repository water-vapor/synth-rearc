from .generator import generate_581f7754
from .verifier import verify_581f7754


TASK_ID = "581f7754"
generate = generate_581f7754
verify = verify_581f7754
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/581f7754.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_581f7754",
    "verify",
    "verify_581f7754",
]
