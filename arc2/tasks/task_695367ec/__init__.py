from .generator import generate_695367ec
from .verifier import verify_695367ec


TASK_ID = "695367ec"
generate = generate_695367ec
verify = verify_695367ec
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/695367ec.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_695367ec",
    "verify",
    "verify_695367ec",
]
