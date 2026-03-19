from .generator import generate_1a244afd
from .verifier import verify_1a244afd


TASK_ID = "1a244afd"
generate = generate_1a244afd
verify = verify_1a244afd
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/1a244afd.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_1a244afd",
    "verify",
    "verify_1a244afd",
]
