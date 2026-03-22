from .generator import generate_8cb8642d
from .verifier import verify_8cb8642d


TASK_ID = "8cb8642d"
generate = generate_8cb8642d
verify = verify_8cb8642d
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/8cb8642d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_8cb8642d",
    "verify",
    "verify_8cb8642d",
]
