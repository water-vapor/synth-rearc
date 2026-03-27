from .generator import generate_2de01db2
from .verifier import verify_2de01db2


TASK_ID = "2de01db2"
generate = generate_2de01db2
verify = verify_2de01db2
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/2de01db2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_2de01db2",
    "verify",
    "verify_2de01db2",
]
