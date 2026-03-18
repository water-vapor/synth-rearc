from .generator import generate_103eff5b
from .verifier import verify_103eff5b


TASK_ID = "103eff5b"
generate = generate_103eff5b
verify = verify_103eff5b
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/103eff5b.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_103eff5b",
    "verify",
    "verify_103eff5b",
]
