from .generator import generate_e872b94a
from .verifier import verify_e872b94a


TASK_ID = "e872b94a"
generate = generate_e872b94a
verify = verify_e872b94a
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e872b94a.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e872b94a",
    "verify",
    "verify_e872b94a",
]
