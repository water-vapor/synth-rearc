from .generator import generate_b0f4d537
from .verifier import verify_b0f4d537


TASK_ID = "b0f4d537"
generate = generate_b0f4d537
verify = verify_b0f4d537
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b0f4d537.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b0f4d537",
    "verify",
    "verify_b0f4d537",
]
