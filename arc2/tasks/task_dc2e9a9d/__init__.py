from .generator import generate_dc2e9a9d
from .verifier import verify_dc2e9a9d


TASK_ID = "dc2e9a9d"
generate = generate_dc2e9a9d
verify = verify_dc2e9a9d
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/dc2e9a9d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dc2e9a9d",
    "verify",
    "verify_dc2e9a9d",
]
