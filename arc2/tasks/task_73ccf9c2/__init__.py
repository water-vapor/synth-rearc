from .generator import generate_73ccf9c2
from .verifier import verify_73ccf9c2


TASK_ID = "73ccf9c2"
generate = generate_73ccf9c2
verify = verify_73ccf9c2
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/73ccf9c2.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_73ccf9c2",
    "verify",
    "verify_73ccf9c2",
]
