from .generator import generate_67636eac
from .verifier import verify_67636eac


TASK_ID = "67636eac"
generate = generate_67636eac
verify = verify_67636eac
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/67636eac.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_67636eac",
    "verify",
    "verify_67636eac",
]
