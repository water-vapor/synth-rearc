from .generator import generate_b20f7c8b
from .verifier import verify_b20f7c8b


TASK_ID = "b20f7c8b"
generate = generate_b20f7c8b
verify = verify_b20f7c8b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/b20f7c8b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_b20f7c8b",
    "verify",
    "verify_b20f7c8b",
]
