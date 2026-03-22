from .generator import generate_917bccba
from .verifier import verify_917bccba


TASK_ID = "917bccba"
generate = generate_917bccba
verify = verify_917bccba
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/917bccba.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_917bccba",
    "verify",
    "verify_917bccba",
]
