from .generator import generate_e99362f0
from .verifier import verify_e99362f0


TASK_ID = "e99362f0"
generate = generate_e99362f0
verify = verify_e99362f0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/e99362f0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_e99362f0",
    "verify",
    "verify_e99362f0",
]
