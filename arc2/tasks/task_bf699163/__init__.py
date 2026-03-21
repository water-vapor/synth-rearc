from .generator import generate_bf699163
from .verifier import verify_bf699163


TASK_ID = "bf699163"
generate = generate_bf699163
verify = verify_bf699163
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/bf699163.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_bf699163",
    "verify",
    "verify_bf699163",
]
