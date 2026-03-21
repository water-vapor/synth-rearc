from .generator import generate_c074846d
from .verifier import verify_c074846d


TASK_ID = "c074846d"
generate = generate_c074846d
verify = verify_c074846d
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/c074846d.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_c074846d",
    "verify",
    "verify_c074846d",
]
