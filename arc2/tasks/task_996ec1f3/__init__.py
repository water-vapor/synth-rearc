from .generator import generate_996ec1f3
from .verifier import verify_996ec1f3


TASK_ID = "996ec1f3"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/996ec1f3.json"

generate = generate_996ec1f3
verify = verify_996ec1f3

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_996ec1f3",
    "verify",
    "verify_996ec1f3",
]
