from .generator import generate_67b4a34d
from .verifier import verify_67b4a34d


TASK_ID = "67b4a34d"
generate = generate_67b4a34d
verify = verify_67b4a34d
REFERENCE_TASK_PATH = "data/official/arc1/evaluation/67b4a34d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_67b4a34d",
    "verify",
    "verify_67b4a34d",
]
