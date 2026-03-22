from .generator import generate_94133066
from .verifier import verify_94133066


TASK_ID = "94133066"
generate = generate_94133066
verify = verify_94133066
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/94133066.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_94133066",
    "verify",
    "verify_94133066",
]
