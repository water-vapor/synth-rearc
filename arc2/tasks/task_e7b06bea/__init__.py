from .generator import generate_e7b06bea
from .verifier import verify_e7b06bea


TASK_ID = "e7b06bea"
generate = generate_e7b06bea
verify = verify_e7b06bea
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e7b06bea.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e7b06bea",
    "verify",
    "verify_e7b06bea",
]
