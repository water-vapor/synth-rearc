from .generator import generate_5ad8a7c0
from .verifier import verify_5ad8a7c0


TASK_ID = "5ad8a7c0"
generate = generate_5ad8a7c0
verify = verify_5ad8a7c0
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/5ad8a7c0.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_5ad8a7c0",
    "verify",
    "verify_5ad8a7c0",
]
