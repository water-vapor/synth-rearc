from .generator import generate_85fa5666
from .verifier import verify_85fa5666


TASK_ID = "85fa5666"
generate = generate_85fa5666
verify = verify_85fa5666
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/85fa5666.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_85fa5666",
    "verify",
    "verify_85fa5666",
]
