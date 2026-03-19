from .generator import generate_e681b708
from .verifier import verify_e681b708


TASK_ID = "e681b708"
generate = generate_e681b708
verify = verify_e681b708
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e681b708.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e681b708",
    "verify",
    "verify_e681b708",
]
