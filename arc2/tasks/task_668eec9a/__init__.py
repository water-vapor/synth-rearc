from .generator import generate_668eec9a
from .verifier import verify_668eec9a


TASK_ID = "668eec9a"
generate = generate_668eec9a
verify = verify_668eec9a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/668eec9a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_668eec9a",
    "verify",
    "verify_668eec9a",
]
