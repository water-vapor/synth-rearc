from .generator import generate_ad173014
from .verifier import verify_ad173014


TASK_ID = "ad173014"
generate = generate_ad173014
verify = verify_ad173014
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ad173014.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ad173014",
    "verify",
    "verify_ad173014",
]
