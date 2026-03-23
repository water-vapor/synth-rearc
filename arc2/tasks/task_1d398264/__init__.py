from .generator import generate_1d398264
from .verifier import verify_1d398264


TASK_ID = "1d398264"
generate = generate_1d398264
verify = verify_1d398264
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1d398264.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1d398264",
    "verify",
    "verify_1d398264",
]
