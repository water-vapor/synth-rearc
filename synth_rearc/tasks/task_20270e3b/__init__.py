from .generator import generate_20270e3b
from .verifier import verify_20270e3b


TASK_ID = "20270e3b"
generate = generate_20270e3b
verify = verify_20270e3b
REFERENCE_TASK_PATH = "data/official/arc2/evaluation/20270e3b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_20270e3b",
    "verify",
    "verify_20270e3b",
]
