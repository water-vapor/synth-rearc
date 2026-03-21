from .generator import generate_cb227835
from .verifier import verify_cb227835


TASK_ID = "cb227835"
generate = generate_cb227835
verify = verify_cb227835
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/cb227835.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cb227835",
    "verify",
    "verify_cb227835",
]
