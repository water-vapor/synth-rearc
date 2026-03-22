from .generator import generate_880c1354
from .verifier import verify_880c1354


TASK_ID = "880c1354"
generate = generate_880c1354
verify = verify_880c1354
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/880c1354.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_880c1354",
    "verify",
    "verify_880c1354",
]
