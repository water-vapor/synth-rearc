from .generator import generate_cfb2ce5a
from .verifier import verify_cfb2ce5a


TASK_ID = "cfb2ce5a"
generate = generate_cfb2ce5a
verify = verify_cfb2ce5a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/cfb2ce5a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_cfb2ce5a",
    "verify",
    "verify_cfb2ce5a",
]
