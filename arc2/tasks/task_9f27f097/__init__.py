from .generator import generate_9f27f097
from .verifier import verify_9f27f097


TASK_ID = "9f27f097"
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/9f27f097.json"

generate = generate_9f27f097
verify = verify_9f27f097

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_9f27f097",
    "verify",
    "verify_9f27f097",
]
