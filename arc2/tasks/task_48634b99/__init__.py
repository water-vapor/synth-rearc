from .generator import generate_48634b99
from .verifier import verify_48634b99


TASK_ID = "48634b99"
generate = generate_48634b99
verify = verify_48634b99
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/48634b99.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_48634b99",
    "verify",
    "verify_48634b99",
]
