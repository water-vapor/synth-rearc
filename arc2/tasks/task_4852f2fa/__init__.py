from .generator import generate_4852f2fa
from .verifier import verify_4852f2fa


TASK_ID = "4852f2fa"
generate = generate_4852f2fa
verify = verify_4852f2fa
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/4852f2fa.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_4852f2fa",
    "verify",
    "verify_4852f2fa",
]
