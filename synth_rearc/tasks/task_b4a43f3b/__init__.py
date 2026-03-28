from .generator import generate_b4a43f3b
from .verifier import verify_b4a43f3b


TASK_ID = "b4a43f3b"
REFERENCE_TASK_PATH = "data/official/arc2/training/b4a43f3b.json"

generate = generate_b4a43f3b
verify = verify_b4a43f3b

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b4a43f3b",
    "verify",
    "verify_b4a43f3b",
]
