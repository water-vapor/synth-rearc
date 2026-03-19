from .generator import generate_1a2e2828
from .verifier import verify_1a2e2828


TASK_ID = "1a2e2828"
generate = generate_1a2e2828
verify = verify_1a2e2828
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1a2e2828.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1a2e2828",
    "verify",
    "verify_1a2e2828",
]
