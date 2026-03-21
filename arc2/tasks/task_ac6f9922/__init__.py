from .generator import generate_ac6f9922
from .verifier import verify_ac6f9922


TASK_ID = "ac6f9922"
generate = generate_ac6f9922
verify = verify_ac6f9922
REFERENCE_TASK_PATH = "arc2_puzzles/data/training/ac6f9922.json"

__all__ = [
    "TASK_ID",
    "REFERENCE_TASK_PATH",
    "generate",
    "generate_ac6f9922",
    "verify",
    "verify_ac6f9922",
]
