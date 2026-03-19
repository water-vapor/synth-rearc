from .generator import generate_dc46ea44
from .verifier import verify_dc46ea44


TASK_ID = "dc46ea44"
generate = generate_dc46ea44
verify = verify_dc46ea44
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/dc46ea44.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_dc46ea44",
    "verify",
    "verify_dc46ea44",
]
