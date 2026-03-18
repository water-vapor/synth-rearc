from .generator import generate_f0100645
from .verifier import verify_f0100645


TASK_ID = "f0100645"
generate = generate_f0100645
verify = verify_f0100645
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/f0100645.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_f0100645",
    "verify",
    "verify_f0100645",
]
