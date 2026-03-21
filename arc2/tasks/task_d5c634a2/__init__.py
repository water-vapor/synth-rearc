from .generator import generate_d5c634a2
from .verifier import verify_d5c634a2


TASK_ID = "d5c634a2"
generate = generate_d5c634a2
verify = verify_d5c634a2
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/d5c634a2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_d5c634a2",
    "verify",
    "verify_d5c634a2",
]
